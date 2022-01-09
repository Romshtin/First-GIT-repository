import names, psycopg2, random

connection = psycopg2.connect(dbname='qa_ddl_24_2', user='user_24_2', password='123', host='159.69.151.133', port='5056')
cursor = connection.cursor()

cursor.execute("drop table public.salary")
connection.commit()
connection.close()
role_id = str(1 + i)

for i in range(30):
    emp_id = str(1 + i)
    s_id = str(random.randint(1, 15))
    insert_query = "insert into public.employee_salary(employee_id, salary_id) values (" + emp_id + "," + s_id + ");"
    cursor.execute(insert_query)
    connection.commit()


for i in range(10):
    emp_id = str(71 + i)
    s_id = str(random.randint(1, 15))
    insert_query = "insert into public.employee_salary(employee_id, salary_id) values (" + emp_id + "," + s_id + ");"
    cursor.execute(insert_query)
    connection.commit()
connection.close()

for i in range(40):
    emp_id = str(1 + i)
    r_r = str(random.choice(list(range(1, 20))))
    insert_query = "insert into public.roles_employee(employee_id, role_id) values (" + emp_id + "," + r_r + ");"
    cursor.execute(insert_query)
    connection.commit()
connection.close()


conn = psycopg2.connect(dbname='qa_ddl_24_2', user='user_24_2', password='123', host='159.69.151.133', port='5056')
cursor = conn.cursor()

if conn:
    select_query = 'select * from public.salary;'
    sql = '''SELECT * FROM salary'''

    cursor.execute(sql)
    column_names = [desc[0] for desc in cursor.description]
    for i in column_names:
        print(i)
    conn.commit()
    conn.close()
execute_q = cursor.execute(select_query)
get_query_result = cursor.fetchall()
print(get_query_result)

for i in get_query_result:
    print('id =', i[0], 'salary =', i[1])

for i in range(10):
    if conn:
        salary = str(6000 + i * 100)
        insert_query = 'insert into public.salary(monthly_salary) values (' + salary + ')'

        cursor.execute(insert_query)
        conn.commit()
cursor.close()
