# Jmeter HW
## HW_1: Отправка запросов на семь эндпоинтов
***
## HW_2
## EX_1:
http://162.55.220.72:5005/user_info

Method: POST

Request (RAW JSON):
```sh
age: int
salary: int
name: str
auth_token: str
```

Response:
```sh
{'start_qa_salary':salary,
 'qa_salary_after_6_months': salary * 2,
 'qa_salary_after_12_months': salary * 2.9,
 'person': {'u_name':[user_name, salary, age],
                                'u_age':age,
                                'u_salary_1.5_year': salary * 4}
                                }
```
### Task:
- Достать Respose значение auth_token из http://162.55.220.72:5005/login, установить его в окружение и использовать в этом запросе
- Достать из Respose значение из поля 'qa_salary_after_6_months' и передать в поле salary запроса http://162.55.220.72:5005/new_data
***
## EX_2:
 http://162.55.220.72:5005/new_data

Method: POST

Request form data:
```sh
age: int
salary: int
name: str
auth_token
```
Response:
```sh
{'name':name,
  'age': int(age),
  'salary': [salary, str(salary*2), str(salary*3)]}
```
Task:
- Достать из Respose значение из поля 'name' и передать в поле name запроса http://162.55.220.72:5005/test_pets_info
