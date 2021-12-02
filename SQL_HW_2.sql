-- 1. Создать таблицу employees
-- id. serial,  primary key,
-- employee_name. Varchar(50), not null

create table employees(
	id serial primary key,
	employee_name varchar(50) not null
)

-- 2. Наполнить таблицу employee 70 строками.
insert into employees(employee_name)
values  (Gregory),
		(Victoria),
		(...);
		
--Через Python быстрее
		
--import psycopg2, names
--
--connection = psycopg2.connect(dbname='qa_ddl_24_2', user='user_24_2', password='123', host='159.69.151.133', port='5056')
--cursor = connection.cursor()
--for i in range(70):
--    name = names.get_first_name()
--    insert_query = "insert into public.employees(employee_name) values ('" + name + "');"
--    cursor.execute(insert_query)
--    connection.commit()
--connection.close()

-- 3. Создать таблицу salary
-- id. Serial  primary key,
-- monthly_salary. Int, not null

create table salary(
	id serial primary key,
	monthly_salary int not null
)

-- 4. Наполнить таблицу salary 15 строками:
--	- 1000
--	- 1100
--	- 1200
--	- 1300
--	- 1400
--	- 1500
--	- 1600
--	- 1700
--	- 1800
--	- 1900
--	- 2000
--	- 2100
--	- 2200
--	- 2300
--	- 2400
--	- 2500

insert into salary(monthly_salary)
values  (1000),
		(1100),
		(...);
		
--Через Python быстрее
		
--import psycopg2
--
--connection = psycopg2.connect(dbname='qa_ddl_24_2', user='user_24_2', password='123', host='159.69.151.133', port='5056')
--cursor = connection.cursor()
--for i in range(15):
--    salary = str(1000 + i * 100)
--    insert_query = "insert into public.salary(monthly_salary) values ('" + salary + "');"
--    cursor.execute(insert_query)
--    connection.commit()
--connection.close()
		
--5. Создать таблицу employee_salary
-- id. Serial  primary key,
-- employee_id. Int, not null, unique
-- salary_id. Int, not null
	
create table employee_salary(
	id serial primary key,
	employee_id int not null unique,
	salary_id int not null
)


-- 6. Наполнить таблицу employee_salary 40 строками:
-- в 10 строк из 40 вставить несуществующие employee_id

insert into employee_salary(employee_id, salary_id)
values 		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
		(7,7),
		(8,8),
		(9,9),
		(...),
		(75, 31),
		(76, 32),
		(77, 33),
		(78, 34),
		(79, 35),
		(81, 36),
		(82, 37),
		(83, 38),
		(84, 39),
		(85, 40);
	
--Python 
	
--import names, psycopg2, random
--
--connection = psycopg2.connect(dbname='qa_ddl_24_2', user='user_24_2', password='123', host='159.69.151.133', port='5056')
--cursor = connection.cursor()
--for i in range(30):
--    emp_id = str(1 + i)
--    s_id = str(random.randint(1, 15))
--    insert_query = "insert into public.employee_salary(employee_id, salary_id) values (" + emp_id + "," + s_id + ");"
--    cursor.execute(insert_query)
--    connection.commit()
--
--
--for i in range(10):
--    emp_id = str(71 + i)
--    s_id = str(random.randint(1, 15))
--    insert_query = "insert into public.employee_salary(employee_id, salary_id) values (" + emp_id + "," + s_id + ");"
--    cursor.execute(insert_query)
--    connection.commit()
--connection.close()
	


-- 7. Создать таблицу roles
-- id. Serial  primary key,
-- role_name. int, not null, unique

create table roles(
	id serial primary key,
	role_name int not null unique
)

-- 8. Поменять тип столба role_name с int на varchar(30)

alter table roles alter column role_name type varchar(30);

-- 9. Наполнить таблицу roles 20 строками

insert into roles(role_name)
values  ('Junior Python developer'),
		('Middle Python developer'),
		('Senior Python developer'),
		('Junior Java developer'),
		('Middle Java developer'),
		('Senior Java developer'),
		('Junior JavaScript developer'),
		('Middle JavaScript developer'),
		('Senior JavaScript developer'),
		('Junior Manual QA engineer'),
		('Middle Manual QA engineer'),
		('Senior Manual QA engineer'),
		('Project Manager'),
		('Designer'),
		('HR'),
		('CEO'),
		('Sales manager'),
		('Junior Automation QA engineer'),
		('Middle Automation QA engineer'),
		('Senior Automation QA engineer');


-- 10. Создать таблицу roles_employee
-- id. Serial  primary key,
-- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
-- role_id. Int, not null (внешний ключ для таблицы roles, поле id)

create table roles_employee(
	id serial primary key,
	employee_id int not null unique,
	foreign key (employee_id)
		references employees(id),
	role_id int not null,
	foreign key (role_id)
		references roles(id)
) 	

-- 11. Наполнить таблицу roles_employee 40 строками

insert into roles_employee(employee_id, role_id)
values  (1, 1),
		(2, 2),
		(...);

--Python
--import psycopg2, random
--
--for i in range(40):
--    emp_id = str(1 + i)
--    r_r = str(random.choice(list(range(1, 20))))
--    insert_query = "insert into public.roles_employee(employee_id, role_id) values (" + emp_id + "," + r_r + ");"
--    cursor.execute(insert_query)
--    connection.commit()
--connection.close()
