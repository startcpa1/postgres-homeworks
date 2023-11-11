CREATE TABLE employees (
	employee_id serial PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	title varchar(100),
	birth_date DATE NOT NULL,
	notes text
);

CREATE TABLE customers (
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(150),
	contact_name varchar(150)
);

CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(10)
	REFERENCES
	customers(customer_id),
	employee_id int REFERENCES
	employees(employee_id),
	order_date DATE NOT NULL,
	ship_city varchar(20)
);