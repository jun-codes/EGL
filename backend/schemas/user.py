from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database.db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True, nullable=False, index=True)

    borrowings = relationship("Borrowing", back_populates="user")
