-- Creating tables for PH-EmployeeDB

CREATE TABLE departments (
	dept_no VARCHAR(4) Not NULL,
	dept_name varchar(40) NOT NULL,
	primary key (dept_no),
	unique (dept_name)
);

Create table employees(
	emp_no int not NULL,
	birth_date date not NULL,
	first_name varchar not NULL,
	last_name varchar not NULL,
	gender varchar not NULL,
	hire_date date not NULL,
	primary key (emp_no)
);

create table dept_manager(
dept_no varchar(4) not NULL,
	emp_no int not NULL,
	from_date date not NULL,
	to_date date not NULL,
foreign key (emp_no) references emoloyees (emp_no),
foreign key (dept_no) references departments (emp_no),
	primary key (emp_no,dept_no)
);

create table salaries(
	emp_no int not NULL,
	salary int not NULL,
	from_date date not NULL,
	foreign key (emp_no) references employees(emp_no),
	primary key (emp_no)
);

create table dept_emp(
	dept_no varchar not NULL,
	emp_no int not NULL,
	from_date date not NULL,
	to_date date not NULL,
	foreign key (emp_no) references employees (emp_no),
	primary key (emp_no)
);

create table titles(
	emp_no int not NULL,
	title varchar not NULL,
	from_date date not NULL,
	to_date date not NULL,
	foreign key (emp_no) references employees (emp_no),
	primary key (emp_no)
);
