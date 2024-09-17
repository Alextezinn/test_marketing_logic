import datetime

from sqlalchemy.orm import sessionmaker, Session

from task_sql.create_tables import Order
from task_sql.create_tables import engine


def insert_orders(session: Session):

    order1 = Order(order_id=1, date=datetime.date(year=2024, month=1, day=1), user_id=1, price=5)
    order2 = Order(order_id=2, date=datetime.date(year=2024, month=1, day=1), user_id=1, price=10)
    order3 = Order(order_id=3, date=datetime.date(year=2024, month=1, day=1), user_id=2, price=5)

    order4 = Order(order_id=4, date=datetime.date(year=2024, month=1, day=1), user_id=3, price=5)
    order5 = Order(order_id=5, date=datetime.date(year=2024, month=1, day=1), user_id=1, price=5)
    order6 = Order(order_id=6, date=datetime.date(year=2024, month=1, day=2), user_id=1, price=5)

    order7 = Order(order_id=7, date=datetime.date(year=2024, month=1, day=2), user_id=2, price=10)
    order8 = Order(order_id=8, date=datetime.date(year=2024, month=1, day=2), user_id=3, price=5)
    order9 = Order(order_id=9, date=datetime.date(year=2024, month=1, day=3), user_id=3, price=5)
    order10 = Order(order_id=10, date=datetime.date(year=2024, month=1, day=3), user_id=3, price=5)

    orders = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10]

    session.add_all(orders)

    session.commit()
    session.close()


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    insert_orders(session)
