from datetime import date
from sqlalchemy import Integer, String, Date
from src.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from static.constants import NAME_LEN, EMAIL_LEN, PHONE_LEN, NOTES_LEN


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(NAME_LEN), nullable=False)
    last_name: Mapped[str] = mapped_column(String(NAME_LEN))
    email: Mapped[str] = mapped_column(String(EMAIL_LEN))
    phone: Mapped[str] = mapped_column(String(PHONE_LEN))
    birthday: Mapped[date] = mapped_column(Date())
    notes: Mapped[str] = mapped_column(String(NOTES_LEN), nullable=True)
