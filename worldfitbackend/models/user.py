from sqlalchemy import Column, Text, Integer
from worldfitbackend.models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)

    hash = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
