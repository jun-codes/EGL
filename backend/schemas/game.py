from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    security_deposit = Column(Integer, default=0)

    borrowings = relationship("Borrowing", back_populates="game")
