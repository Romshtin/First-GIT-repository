import requests, json

url = 'http://162.55.220.72:5005/'
resp_hello = requests.get(url)

print('resp_hello =', resp_hello.text)

resp_hello_headers = resp_hello.headers

for key, value in resp_hello_headers.items():
    print('key =', key)
    print('value =', value)
    print('===================')

url_first = url + 'first'
resp_first = requests.get(url_first)
print('resp_first =', resp_first.text)

end_point_get_method = 'get_method'
url_get_method = url + end_point_get_method

get_method_params = {'name': 'Anastasiya',
                     'age': 18}

resp_get_method = requests.get(url_get_method, params=get_method_params)
print('resp_get_method =', resp_get_method.json())

url_login = url + 'login'

login_data = {'login': 'Roman',
              'password': 34}

resp_login = requests.post(url_login, data=login_data)
user_token = resp_login.json()['token']
print(user_token)

url_user_info_1 = url + 'user_info'


user_info_1_data = {'name': 'Roman',
                    'age': 25,
                    'salary': 50000,
                    'auth_token': user_token}

json_data = json.dumps(user_info_1_data)
req_headers = {'Content-type': 'application/json'}

resp_post_user_info_1 = requests.post(url_user_info_1, data=json_data, headers=req_headers)
resp_user_info_json = resp_post_user_info_1.json()

for key, value in resp_user_info_json.items():
    print('key', key, )
    print('value', value)
    print('===================')