from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('postgresql://snacks@localhost/snacks', echo=True)


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     password = Column(String)

#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', password='%s')>" % (
#             self.name, self.fullname, self.password)


class Marathon(Base):
    __tablename__ = 'marathon'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)
    bought = Column(DateTime(timezone=True))
    eaten = Column(DateTime(timezone=True))


Base.metadata.create_all(engine)
