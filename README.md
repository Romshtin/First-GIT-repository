# Jmeter HW
## HW_1: Отправка запросов на семь эндпоинтов
***
## HW_2
http://162.55.220.72:5005/user_info

request (RAW JSON)

POST

age: int

salary: int

name: str

auth_token


response:
```sh
{'start_qa_salary':salary,
 'qa_salary_after_6_months': salary * 2,
 'qa_salary_after_12_months': salary * 2.9,
 'person': {'u_name':[user_name, salary, age],
                                'u_age':age,
                                'u_salary_1.5_year': salary * 4}
                                }
```
### Task
- Достать из Respose значение из поля 'qa_salary_after_6_months' и передать в поле salary запроса http://162.55.220.72:5005/new_data
***
