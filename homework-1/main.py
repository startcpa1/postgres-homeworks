from utils import fill_table_employees, fill_table_customers, fill_table_orders, get_data_from_csv

data = get_data_from_csv('employees_data.csv')
data1 = get_data_from_csv('customers_data.csv')
data2 = get_data_from_csv('orders_data.csv')

fill_table_employees(data, 'employees')
fill_table_customers(data1, 'customers')
fill_table_orders(data2, 'orders')
