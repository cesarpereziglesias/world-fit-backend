from Crypto.Hash import SHA256
from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship, backref

from worldfitbackend.models import Base, DBSession

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)

    hash = Column(Text, nullable=False)
    mail = Column(Text, nullable=False)

    activities = relationship("Activity", backref="user")

    def __init__(self, mail):
        self.mail = mail
        self.hash = User.create_hash(mail)

    def to_dict(self):
        return {"mail": self.mail,
                "hash": self.hash}

    @staticmethod
    def create_hash(mail):
        return SHA256.new(mail).hexdigest()

    @staticmethod
    def get_by_hash(user_hash):
        return DBSession.query(User).filter_by(hash=user_hash).first()
