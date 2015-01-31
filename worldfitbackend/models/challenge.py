from sqlalchemy import Column, Integer, Text
from worldfitbackend.models import Base

class Challenge(Base):
    __tablename__ = 'challenges'

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(Text, nullable=False)
