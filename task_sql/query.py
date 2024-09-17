from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from task_sql.create_tables import engine


def main():
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1 вариант sql-запроса
    result = session.execute(text(
        """
        SELECT
        DATE,
        COUNT(*) AS Количество_заказов,
        (SELECT COUNT(*)
        FROM (SELECT DISTINCT USER_ID
        FROM orders o2
        WHERE o2.DATE = o.DATE) t) AS Количество_покупателей,
        SUM(PRICE) AS Оборот
        FROM orders o
        GROUP BY DATE
        ORDER BY DATE;
        """
    ))

    rows = result.fetchall()
    for row in rows:
        print(row)

    print()

    # 2 вариант sql-запроса
    result = session.execute(text(
        """
        SELECT
        DATE,
        (SELECT COUNT(*) FROM orders o1 WHERE o1.DATE = o.DATE) AS Количество_заказов,
        (SELECT COUNT(DISTINCT USER_ID) FROM orders o2 WHERE o2.DATE = o.DATE) AS Количество_покупателей,
        (SELECT SUM(PRICE) FROM orders o3 WHERE o3.DATE = o.DATE) AS Оборот
    FROM
        orders o
    GROUP BY
        DATE
    ORDER BY
        DATE;
        """
    ))

    rows = result.fetchall()
    for row in rows:
        print(row)

    session.close()


if __name__ == "__main__":
    main()
