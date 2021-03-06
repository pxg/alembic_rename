from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('postgresql://snacks@localhost/snacks', echo=True)


class Marathon(Base):
    __tablename__ = 'snickers'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)
    bought = Column(DateTime(timezone=True), nullable=False)
    eaten = Column(DateTime(timezone=True), nullable=False)

# Not needed as we're using alembic
#Base.metadata.create_all(engine)
