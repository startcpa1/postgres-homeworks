import psycopg2

from utils import fill_table_employees, fill_table_customers, fill_table_orders, get_data_from_csv


def main():
    """Открываем соединение и вызываем функции"""
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')

    data_employees = get_data_from_csv('employees_data.csv')
    data_customers = get_data_from_csv('customers_data.csv')
    data_orders = get_data_from_csv('orders_data.csv')

    fill_table_employees(conn, data_employees)
    fill_table_customers(conn, data_customers)
    fill_table_orders(conn, data_orders)

    conn.close()


if __name__ == "__main__":
    main()
