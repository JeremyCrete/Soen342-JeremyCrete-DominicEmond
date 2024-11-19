from sqlalchemy import Column, Integer, String, Enum, Boolean
from database import Base
from Model.Type import Type

class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mode = Column(String, nullable=False)
    lesson_type = Column(Enum(Type), nullable=False)  # Use the Type Enum here
    is_active = Column(Boolean, default=True, nullable=False)  # Add the 'is_active' column

    def __init__(self, mode, lesson_type, is_active=True):
        self.mode = mode
        self.lesson_type = lesson_type
        self.is_active = is_active  # Assign the is_active value

    def __repr__(self):
        return f"Lesson(mode={self.mode}, lesson_type={self.lesson_type}, is_active={self.is_active})"
