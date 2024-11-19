from sqlalchemy import Column, Integer, String, Enum
from database import Base
from Model.Type import Type

class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True, autoincrement=True)
    mode = Column(String, nullable=False)
    lesson_type = Column(Enum(Type), nullable=False)  # Use the Type Enum here

    def __init__(self, mode, lesson_type):
        self.mode = mode
        self.lesson_type = lesson_type

    def __repr__(self):
        return f"Lesson(mode={self.mode}, lesson_type={self.lesson_type})"
