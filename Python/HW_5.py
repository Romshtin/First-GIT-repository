import random, math, names, randomtimestamp, datetime, string

# Python HW 5 Functions, Lists
#  - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.
#
# 1) Написать скрипт который в создаст список целых чисел.

int_list = list(range(71))
print(int_list)

# 2) Написать скрипт который в создаст список целых чётных чисел.

int_even_list = list(range(0, 140, 2))
print(int_even_list)

int_even_list = []
while len(int_even_list) < 70:
    rand = random.randint(0, 1000)
    if rand % 2 == 0:
        int_even_list.append(rand)
print(int_even_list)

# 3) Написать скрипт который в создаст список целых нечётных чисел.

int_odd_list = list(range(1, 140, 2))
print(int_odd_list)

int_odd_list = []
while len(int_odd_list) < 70:
    rand = random.randint(0, 1000)
    if rand % 2:
        int_odd_list.append(rand)
print(int_odd_list)

# 4) Написать скрипт который из списка целых чисел выведет чётные числа.

even_n_from_int_list = []
for i in int_list:
    if i % 2 == 0:
        even_n_from_int_list.append(i)
print(even_n_from_int_list)

# 5) Написать скрипт который из списка целых чисел выведет нечётные числа.

odd_n_from_int_list = []
for j in int_list:
    if j % 2:
        odd_n_from_int_list.append(j)
print(odd_n_from_int_list)

# 6) Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.

even_n_1_from_int_list = []
for k in int_list:
    if k % 2 == 0 and k % 5 == 0:
        even_n_1_from_int_list.append(k)
print(even_n_1_from_int_list)

# 7) Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.

count = 0
for _ in int_list:
    if _ % 2 == 0 and _ % 5 == 0:
        count += 1
print(count)

# 8) Написать скрипт который в создаст список целых рандомных чисел.

int_random_list = [random.randint(0, 1000) for _ in range(70)]
print(int_random_list)

# 9) Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.


def div_5(list):
    list_parts = []
    new_full_list = []
    count = 0
    for i in list:
        count += 1
        if count < 5:
            list_parts.append(i)
        else:
            list_parts.append(i)
            new_full_list.append(list_parts)
            list_parts = []
            count = 0
    return new_full_list


print(div_5(int_list))


def div(list, n):
    full_list = []
    list_size = len(list) / n
    for i in range(int(list_size)):
        full_list.append(list[n * i: n * (i + 1)])
    return full_list


print(div(int_list, 5))


def split(list, size):
    new_list = []
    while len(list) > size:
        peace = list[:size]
        new_list.append(peace)
        list = list[size:]
    return new_list


print(split(int_list, 5))

# 10) Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.


def even_odd_sep(list):
    even_list = []
    odd_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


print(even_odd_sep(int_list))


# 11) Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.

stars_5 = []
temp_stars_5 = []

for i in range(70):
    if len(temp_stars_5) < 4:
        temp_stars_5.append(i)
    else:
        temp_stars_5.append(i)
        stars_5.append(temp_stars_5)
        temp_stars_5 = []
print(stars_5)

# 12) Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars

stars_5_sum = []
for j in stars_5:
    stars_5_sum.append(sum(j))
print(stars_5_sum)

# 13) Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”


def div_on_2(list):
    list_sum_more_or_even_100 = []
    list_sum_less_100 = []

    for j in (list):
        if sum(j) >= 100:
            list_sum_more_or_even_100.append(sum(j))
        elif sum(j) < 100:
            list_sum_less_100.append(sum(j))
        else:
            print('No lists')
    return list_sum_more_or_even_100, list_sum_less_100


print(div_on_2(stars_5))

# 14) Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.

def savings(age):
    money_left_after_spendings = 140
    month_to_10000 = math.ceil(10000 / money_left_after_spendings)
    month_to_20000 = math.ceil(20000 / money_left_after_spendings)
    month_to_30000 = math.ceil(30000 / money_left_after_spendings)
    month_to_50000 = math.ceil(50000 / money_left_after_spendings)
    month_to_100000 = math.ceil(100000 / money_left_after_spendings)

    print('After', month_to_10000, 'months i will have 10000$')
    print('After', month_to_20000, 'months i will have 20000$')
    print('After', month_to_30000, 'months i will have 30000$')
    print('After', month_to_50000, 'months i will have 50000$')
    print('After', month_to_100000, 'months i will have 100000$')


savings(25)

# 15) Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA. Free implementation of function body logic


def salary_growth(starting_salary, experience):
    Python = starting_salary * 0.25
    Postman = starting_salary * 0.25
    Communication = starting_salary * 0.3
    Trainings_mittings_performance = starting_salary * 0.2
    roadmap = [Python, Postman, Communication, Trainings_mittings_performance]
    result = starting_salary + sum(roadmap) * experience
    print(result)


salary_growth(35000, 1)

# 16) Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.

for _ in range(70):
    name = names.get_first_name()
    print(name)

# 17) Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.

for i in range(1, 70):
    filename = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    print(i, '-', filename)

#  18) Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.

# start = datetime.datetime.strptime("21-06-2014", "%d-%m-%Y")
# end = datetime.datetime.strptime("07-07-2014", "%d-%m-%Y")
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
#
# for date in date_generated:
#     print(date.strftime("%d-%m-%Y"))

names_and_date = []
res = []
for i in range(4):
    name = names.get_full_name()
    date = randomtimestamp.random_date()
    res.append(name)
    res.append(date.strftime('%d-%m-%Y'))
    names_and_date.append(res)
    res = []

print(names_and_date)

# 19) Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации

Employees = []
res = []
for _ in range(70):
    name = names.get_first_name()
    login = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))
    domen = ['@mail.ru', '@gmail.com', '@hotmail.com', '@aol.com', '@mail.com', '@mail.kz', '@yahoo.com']
    email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + random.choice(domen)
    date = randomtimestamp.random_date()
    res.append(name)
    res.append(login)
    res.append(password)
    res.append(email)
    res.append(date.strftime('%d-%m-%Y'))
    Employees.append(res)
    res = []
print(Employees)

# 20) Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно),

family = []
res = []
for _ in range(70):
    login = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    m_name = names.get_first_name('male') + ' - ' + 'м'
    f_name = names.get_first_name('female') + ' - ' + 'ж'
    random_name = [m_name, f_name]
    name = random.choice(random_name)
    family_status_res = ['Cемейный статус - True', 'Cемейный статус - False']
    family_status = random.choice(family_status_res)
    res.append(login)
    res.append(name)
    res.append(family_status)
    family.append(res)
    res = []
print(family)

# 21) Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)

gender = []
res = []
for _ in range(10):
    login = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    m_name = names.get_first_name('male')
    f_name = names.get_first_name('female')
    random_name = [m_name, f_name]
    name = random.choice(random_name)
    res.append(login)
    res.append(name)
    if name == m_name:
        res.append('м')
    else:
        res.append('ж')
    gender.append(res)
    res = []
print(gender)

# 22) Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)

salary = []
res = []
for _ in range(70):
    login = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    m_name = names.get_first_name('male') + ' - ' + 'м'
    f_name = names.get_first_name('female') + ' - ' + 'ж'
    random_name = [m_name, f_name]
    name = random.choice(random_name)
    salary_ = str(random.randint(300, 5000)) + '$'
    res.append(login)
    res.append(name)
    res.append(salary_)
    salary.append(res)
    res = []
print(salary)

# 23) Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$

salary_range = []
for i in salary:
    if '1500$' <= i[2] <= '3000$':
        salary_range.append(i)
print(salary_range)

# 24) Написать скрипт который создаст список имён мужчин из gender.

gender_m = []
for i in gender:
    if i[2] == 'м':
        gender_m.append(i[1])
print(gender_m)

# 25) Написать скрипт который создаст список имён женщин из gender.

gender_w = []
for i in gender:
    if i[2] == 'ж':
        gender_w.append(i[1])
print(gender_w)

# 26) Написать скрипт который создаст список имён неженатых мужчин из family.

single_man = []
for i in family:
    if 'м' in i[1]:
        single_man.append(i[1])
print(single_man)

# 27) Написать скрипт который создаст список имён незамужних женщин из family.

single_woman = []
for i in family:
    if 'ж' in i[1]:
        single_woman.append(i[1])
print(single_woman)

# 28) Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций

odinoki_boec = []
shirokoi_dushi_chelovek = []

for i in family:
    if 'False' in i[2] and 'м' in i[1]:
        odinoki_boec.append(i[1])

for j in salary:
    if j[2] >= '1500$' and 'м' in j[1]:
        shirokoi_dushi_chelovek.append(j[1])

zhelanni_zhenih = list(set(odinoki_boec) & set(shirokoi_dushi_chelovek))
print(zhelanni_zhenih)

# 29) Реализуйте пункт 28 через через функции.


def naiti_hal9vy(gender, bablo):

    odinoki_boec = []
    shirokoi_dushi_chelovek = []

    for i in family:
        if 'False' in i[2] and gender in i[1]:
            odinoki_boec.append(i[1])

    for j in salary:
        if j[2] >= bablo and gender in j[1]:
            shirokoi_dushi_chelovek.append(j[1])

    zhelanni_chelovek = list(set(odinoki_boec) & set(shirokoi_dushi_chelovek))
    return zhelanni_chelovek


print(naiti_hal9vy('м', '1500$'))

# 30) Поешьте и выспитесь)
