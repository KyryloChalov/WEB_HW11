from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.schemas import ContactModel, ContactResponse
from typing import List

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("/", response_model=ContactResponse)
async def create_contact(contact: ContactModel, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(contact, db)


# всі контакти без зайвих питань - чи воно треба?
# @router.get("/", response_model=List[ContactResponse])
# async def read_all_contacts(db: Session = Depends(get_db)):
#     contacts = await repository_contacts.read_contacts(db)
#     return contacts


# пошук рядка find_string в полях first_name, last_name, email
# якшо рядок пошуку порожній - виводяться всі контакти
@router.get("/", response_model=List[ContactResponse])
async def read_contacts(db: Session = Depends(get_db), find_string: str = ""):
    contacts = await repository_contacts.read_contacts(db, find_string)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def find_contact_id(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.find_contact(contact_id, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    contact_id: int, contact: ContactModel, db: Session = Depends(get_db)
):
    contact = await repository_contacts.update_contact(contact_id, contact, db)
    return contact


@router.delete("/{contact_id}")
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id, db)
    return contact


@router.get("/birthdays/", response_model=List[ContactResponse])
async def get_week_birthdays(db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_week_birthdays(db)
    return contacts
