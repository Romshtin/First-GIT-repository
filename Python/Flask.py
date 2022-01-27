from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)


# гайд по запуску сервера
# https://docs.google.com/document/d/1EftxFRwEsMy5k5WPixkeYkzecQhE_H3p/edit?usp=sharing&ouid=103542583675412644697&rtpof=true&sd=true


@app.route("/")  # декоратор
def first():
    return "Greetings!"


@app.route("/user_info", methods=["GET", "POST", "DELETE"])
def user_info():
    name = request.args.get('name')
    age = request.args.get('age')
    user_list = [name, age]

    return jsonify(user_list)


@app.route("/user_info_1", methods=["POST"])
def user_info_1():
    name = request.form.get('name')
    age = request.form.get('age')
    salary = int(request.form.get("salary"))
    annually = str(salary * 12)

    resp_str = {"name": name,
                "age": age,
                "annually": annually}

    return jsonify(resp_str)


@app.route("/user_info_2", methods=["POST"])
def user_info_2():
    name = request.json['name']
    age = request.json['age']
    salary = int(request.json["salary"])
    annually = str(salary * 12)

    resp_str = {"name": name,
                "age": age,
                "annually": annually}

    return jsonify(resp_str)


@app.route("/take_url_param", methods=["GET"])
def take_url_params():
    q_str = str(request.url)
    url_params = q_str.split("os=")[-1].split("&model")[0]

    return jsonify(url_params)


conn = psycopg2.connect(dbname='qa_ddl_24_2', user='user_24_2', password='123', host='159.69.151.133', port='5056')


@app.route("/db_save", methods=["GET", "POST"])
def db_save():

    id = request.args.get('employee_id')
    role = request.args.get('role_id')

    cursor = conn.cursor()

    if conn:
        base_data = (id, role)
        insert_query = """insert into public.roles_employee(employee_id, role_id) values (%s,%s);"""
        cursor.execute(insert_query, base_data)
        conn.commit()
        cursor.close()

        return "User saved"

    else:
        return "User hasn't been saved"


@app.route('/roles')
def roles():

    result = {}

    cursor = conn.cursor()

    if conn:
        sl = cursor.execute("""select employees.id, employee_name, role_name, monthly_salary 
                                    from public.roles_employee
                                    join employees on roles_employee.employee_id = employees.id
                                    join roles on roles.id = roles_employee.role_id
                                    join employee_salary on employee_salary.employee_id = employees.id
                                    join salary on salary.id = employee_salary.salary_id
                                    where monthly_salary between 1700 and 2300 order by monthly_salary;""")
        sll = cursor.fetchall()
        for i in sll:
            result[i[0]] = {'Employee_name': i[1], 'Role_name': i[2], 'Monthly_salary': i[3]}
        cursor.close()

        return jsonify(result)

    else:
        return "Connection error"
