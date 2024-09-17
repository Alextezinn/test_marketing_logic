from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:postgres@localhost:5432/test')
Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    date = Column(Date)
    user_id = Column(Integer)
    price = Column(Integer)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
