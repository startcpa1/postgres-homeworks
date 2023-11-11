import csv
import os

import psycopg2


def get_data_from_csv(filename):
    """Открываем файл, получаем данные, возвращаем список словарей"""
    file_path = os.path.join(
        'north_data', filename)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = csv.DictReader(f)
        return list(data)


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')


def fill_table_employees(data):
    """Записываем в таблицу employees данные из списка словарей """
    cur = conn.cursor()
    for el in data:
        cur.execute(
            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s);",
            (el['employee_id'], el['first_name'], el['last_name'], el['title'], el['birth_date'], el['notes']))
        conn.commit()


def fill_table_customers(data):
    """Записываем в таблицу customers данные из списка словарей """
    cur = conn.cursor()
    for el in data:
        cur.execute(
            "INSERT INTO customers VALUES (%s, %s, %s);",
            (el['customer_id'], el['company_name'], el['contact_name']))
        conn.commit()


def fill_table_orders(data):
    """Записываем в таблицу orders данные из списка словарей """
    cur = conn.cursor()
    for el in data:
        cur.execute(
            "INSERT INTO orders VALUES (%s, %s, %s, %s, %s);",
            (el['order_id'], el['customer_id'], el['employee_id'], el['order_date'], el['ship_city']))
        conn.commit()
