from utils import fill_table_employees, fill_table_customers, fill_table_orders, get_data_from_csv

data_employees = get_data_from_csv('employees_data.csv')
data_customers = get_data_from_csv('customers_data.csv')
data_orders = get_data_from_csv('orders_data.csv')

fill_table_employees(data_employees)
fill_table_customers(data_customers)
fill_table_orders(data_orders)
