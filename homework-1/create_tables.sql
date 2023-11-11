CREATE TABLE employees (
	employee_id serial PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date DATE NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers (
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(150) NOT NULL,
	contact_name varchar(150) NOT NULL
);

CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(150) NOT NULL,
	employee_id int NOT NULL,
	order_date DATE NOT NULL,
	ship_city varchar(20)
);