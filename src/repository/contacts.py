from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, extract
from src.database.models import Contact
from src.database.db import get_db
from src.schemas import ContactModel
from datetime import timedelta
from typing import List


async def create_contact(contact: ContactModel, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


async def read_contacts(db: Session = Depends(get_db), q: str = ""):
    if q:
        return (
            db.query(Contact)
            .filter(
                or_(
                    Contact.first_name.ilike(f"%{q}%"),
                    Contact.last_name.ilike(f"%{q}%"),
                    Contact.email.ilike(f"%{q}%"),
                )
            )
            .all()
        )
    return db.query(Contact).all()


async def find_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == int(contact_id)).first()
    if db_contact is None:
        raise HTTPException(
            status_code=404, detail=f"Contact with id: {contact_id} was not found"
        )
    return db_contact


async def update_contact(id: int, body: ContactModel, db: Session):
    contact = db.query(Contact).filter(Contact.id == id).first()
    if contact:
        for key, value in body.model_dump().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(
            status_code=404, detail=f"Contact with id: {contact_id} was not found"
        )
    db.delete(db_contact)
    db.commit()
    return {"message": "Contact successfully deleted"}


async def get_week_birthdays(db: Session = Depends(get_db)):
    today = datetime.now().date()
    end_date = today + timedelta(days=7)

    result = (
        db.query(Contact)
        .filter(
            or_(
                and_(
                    extract("month", Contact.birthday) == today.month,
                    extract("day", Contact.birthday) >= today.day,
                    extract("day", Contact.birthday) <= end_date.day,
                ),
                and_(
                    extract("month", Contact.birthday) == end_date.month,
                    extract("day", Contact.birthday) >= today.day,
                    extract("day", Contact.birthday) <= end_date.day,
                ),
            )
        )
        .all()
    )
    return result
