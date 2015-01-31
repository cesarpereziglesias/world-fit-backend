from sqlalchemy import Column, Integer, DateTime, Text
from worldfitbackend.models import Base

class Challenge(Base):
    __tablename__ = 'challenges'

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(Text, nullable=False)
    owner = Column(Text, nullable=False)
    challenge_type = Column(Text, nullable=False)
    init = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "owner": self.owner,
                "challenge_type": self.challenge_type,
                "init": self.init.strftime("%Y/%m/%d"),
                "end": self.end.strftime("%Y/%m/%d")}
