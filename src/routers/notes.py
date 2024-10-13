from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from src import models, schemas, database
from src.routers.users import get_current_user

router = APIRouter()


@router.post("/", response_model=schemas.Note, status_code=status.HTTP_201_CREATED)
def create_note(
        note: schemas.NoteCreate,
        db: Session = Depends(database.get_db),
        user: models.User = Depends(get_current_user)
):
    db_note = models.Item(**note.dict())
    db_note.users.append(user)  # Establish relationship with the user
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.get("/", response_model=List[schemas.Note])
def read_notes(
        db: Session = Depends(database.get_db),
        user: models.User = Depends(get_current_user),
        skip: int = 0, limit: int = 10
):
    notes = (
        db.query(models.Item)
        .filter(models.Item.users.contains([user]), models.Item.is_deleted == False)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return notes


@router.get("/{note_id}", response_model=schemas.Note)
def read_note(
        note_id: UUID,
        db: Session = Depends(database.get_db),
        user: models.User = Depends(get_current_user)
):
    note = (
        db.query(models.Item)
        .filter(models.Item.item_id == note_id, models.Item.users.contains([user]))
        .first()
    )
    if not note or note.is_deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=schemas.Note)
def update_note(
        note_id: UUID,
        note_data: schemas.NoteCreate,
        db: Session = Depends(database.get_db),
        user: models.User = Depends(get_current_user)
):
    note = (
        db.query(models.Item)
        .filter(models.Item.item_id == note_id, models.Item.users.contains([user]))
        .first()
    )
    if not note or note.is_deleted:
        raise HTTPException(status_code=404, detail="Note not found")

    # Update note fields
    for key, value in note_data.dict().items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
        note_id: UUID,
        db: Session = Depends(database.get_db),
        user: models.User = Depends(get_current_user)
):
    note = (
        db.query(models.Item)
        .filter(models.Item.item_id == note_id, models.Item.users.contains([user]))
        .first()
    )
    if not note or note.is_deleted:
        raise HTTPException(status_code=404, detail="Note not found")

    # Soft-delete the note by setting is_deleted to True
    note.is_deleted = True
    db.commit()
    return
