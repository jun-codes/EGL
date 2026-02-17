from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Borrowing(Base):
    __tablename__ = "borrowings"

    borrow_id = Column(Integer, primary_key=True, index=True)

    game_id = Column(Integer, ForeignKey("games.game_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    borrow_datetime = Column(DateTime, nullable=False)
    expected_return_datetime = Column(DateTime, nullable=False)
    actual_return_datetime = Column(DateTime)

    status = Column(String, nullable=False)  # Borrowed / Returned / Late

    user = relationship("User", back_populates="borrowings")
    game = relationship("Game", back_populates="borrowings")
