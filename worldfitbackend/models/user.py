from Crypto.Hash import SHA256
from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship, backref

from worldfitbackend.models import Base, DBSession

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)

    hash = Column(Text, nullable=False)
    email = Column(Text, nullable=False)

    activities = relationship("Activity", backref="user")

    def __init__(self, email):
        self.email = email
        self.hash = User.create_hash(email)

    def to_dict(self):
        return {"email": self.email,
                "hash": self.hash}

    @staticmethod
    def create_hash(email):
        return SHA256.new(email).hexdigest()

    @staticmethod
    def get_by_hash(user_hash):
        return DBSession.query(User).filter_by(hash=user_hash).first()
