from fastapi import FastAPI, Depends, HTTPException
from other.seed import seed_data
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.database.db import get_db, reset_db
from src.routes import contacts

import uvicorn

app = FastAPI()


app.include_router(contacts.router, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": "Welcome! This is Homework 11"}


@app.delete("/reset_base")
async def reset_database():
    reset_db()
    return {"message": "Congratulations! You have a new database"}


@app.get("/healthchecker")
async def healthchecker(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(
                status_code=502, detail="Database is not configured correctly"
            )
        return {"message": "Congratulations! Database is really healthy"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=502, detail="Error connecting to the database")


@app.post("/seed")
async def seed_fake_data(number_contacts: int = 10):
    seed_data(number_contacts)
    return {"message": f"You have {number_contacts} new fake Contacts"}


if __name__ == "__main__":
    uvicorn.run(app)

# cmd:
# uvicorn main:app --host localhost --port 8000 --reload
# docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=8811550 -d postgres
