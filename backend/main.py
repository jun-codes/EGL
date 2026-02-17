from fastapi import FastAPI

from backend.database.db import SessionLocal, Base, engine
from backend.schemas.user import User
from backend.schemas.game import Game
from backend.schemas.borrowings import Borrowing


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"status": "backend running"}

from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database.db import SessionLocal
from backend.schemas.user import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, email: str, phone: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email, phone=phone)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

