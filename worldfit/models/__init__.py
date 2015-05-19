# -*- coding: utf-8 -*-
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

class Base(object):

    @classmethod
    def get_by_id(cls, id):
        return DBSession.query(cls).get(id)

    @classmethod
    def get_columns(cls):
        return [column.key for column in inspect(cls).attrs]

    def to_dict(self):
        # TODO: How to use a json encoder
        return dict((column, getattr(self, column)) for column in self.get_columns())

    def __str__(self):
        return "[%s(%s)]" % (self.__class__.__name__, ', '.join('%s=%s' % (k, self.__dict__[k]) for k in sorted(self.__dict__) if '_sa_' != k[:4]))

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base(cls=Base)

# Include models
__all__ = []
