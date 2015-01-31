from sqlalchemy import Table, Column, Integer, ForeignKey
from worldfitbackend.models import Base

Suscription = Table('suscriptions', Base.metadata,
    Column('challenge_id', Integer, ForeignKey('challenges.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)
