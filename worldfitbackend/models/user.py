import json
from Crypto.Hash import SHA256
from sqlalchemy import Column, Text, Integer

from worldfitbackend.models import Base, DBSession

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)

    hash = Column(Text, nullable=False)
    email = Column(Text, nullable=False)

    def __init__(self, email):
        self.email = email
        self.hash = User.create_hash(email)


    def to_json(self):
        return json.dumps({"email": self.email,
                           "hash": self.hash})

    @staticmethod
    def create_hash(email):
        return SHA256.new(email).hexdigest()

    @staticmethod
    def get_by_hash(user_hash):
        return DBSession.query(User).filter_by(hash=user_hash).first()
