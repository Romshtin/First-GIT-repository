from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

driver.get('https://fh.by/')  # coockie _gcl_au=1.1.550512313.1640717555; _ym_uid=1640717555644445970; _ym_d=1640717555; _ym_isad=1; _ga=GA1.2.2118182948.1640717555; _gid=GA1.2.1226181697.1640717555; ab_id=5e9e67fb5a805fad8cdf1eda87160f894fdf5439; mindboxDeviceUUID=41df55a7-49c0-4f22-92aa-fb8ec03126e2; directCrm-session=%7B%22deviceGuid%22%3A%2241df55a7-49c0-4f22-92aa-fb8ec03126e2%22%7D; _gat_UA-154554678-1=1
driver.add_cookie({'cookie': 'eyJzb3VyY2UiOiJ3ZWIiLCJ0b2tlbiI6IjJTRTJFSUtwS1hPRHlvMm5XUG1CYyIsInRpbWVzdGFtcCI6MTY0MDcxNzU0OTM3MX0%3D'})

# driver = webdriver.Chrome("./chromedriver.exe", options=options)


login_page = driver.find_element(By.LINK_TEXT, 'Войти').click()
# print(login_button.get_attribute('innerHTML'))
time.sleep(2)


phone_field = driver.find_element(By.NAME, 'phone')
phone_field.send_keys('123132511')  # 296091336
time.sleep(5)


login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/div/div[2]/button').click()

time.sleep(2)


verification_code = driver.find_element(By.NAME, 'verification_code')
verification_code.send_keys('1234')

button_enter = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div/form/div[3]/button').click()


phone_field = driver.find_element(By.NAME, 'phone')
phone_field.send_keys('')
time.sleep(2)


name_field = driver.find_element(By.ID, 'name')
name_field.send_keys('Roman')
time.sleep(1)

surname_field = driver.find_element(By.ID, 'surname')
surname_field.send_keys('Kirillov')
time.sleep(1)

email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('kirillov4@mail.ru')
time.sleep(1)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('Qwerty123!')

submit = driver.find_element(By.TAG_NAME, 'button')
submit.click()
time.sleep(1)

success_message = driver.find_element(By.TAG_NAME, 'strong')
print(success_message.text)

message_path = '/html/body/div[2]/div/div/div/strong'
success_message_2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/strong')

if 'Success' in success_message_2.text:
    print('Test passed')
else:
    print('Test failed')

time.sleep(3)

driver.close()