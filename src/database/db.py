from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:8811550@localhost:5432/postgres"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

def reset_db():
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine)
    # Base.metadata.bind = engine

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
