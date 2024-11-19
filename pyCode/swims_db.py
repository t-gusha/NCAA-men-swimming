from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date

engine = create_engine('sqlite:///swims.db?check_same_thread=False')
Base = declarative_base()


class FreestyleMenNCAA(Base):
    __tablename__ = 'swims'

    id = Column(Integer, primary_key=True)
    Place = Column(Integer)
    Time = Column(Float)
    Year = Column(Integer)
    School =  Column(String)

Base.metadata.create_all(engine)
print('Action Complete')