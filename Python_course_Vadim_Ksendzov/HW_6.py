import csv, names, random, randomtimestamp as rt, datetime
# Python CSV
#
#
# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
#
#
# 1) Создать пустой empty.csv файл.

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov\empty.csv"

with open(file_name, 'w') as fn:
    pass

# 2) Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov\digits.csv"

with open(file_name, 'w') as fn:
    writer = csv.writer(fn, lineterminator='\n')
    for i in range(151):
        writer.writerow([i])

# 3) Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/names.csv"

with open(file_name, 'w') as fn:
    writer = csv.writer(fn, lineterminator='\n')
    for i in range(100):
        writer.writerow([names.get_first_name()])

# 4) Вариант 1. Создать emails.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/emails.csv"

with open(file_name, 'w') as fn:
    writer = csv.writer(fn, lineterminator='\n')
    for i in range(100):
        writer.writerow([names.get_last_name() + str(i) + '@gmail.com'])

# 5) Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк.
# Имя и часть email до @ должны совпадать.

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/nne.csv"

with open(file_name, 'w') as fn:
    columns = ['Number', 'Name', 'Email']
    writer = csv.DictWriter(fn, fieldnames=columns, lineterminator='\n')
    writer.writeheader()
    for i in range(100):
        r = random.randint(100000000, 999999999)
        number = '89' + str(r)
        name = names.get_first_name()
        Email = name + '@gmail.com'
        row = {'Number': number, 'Name': name, 'Email': Email}
        writer.writerow(row)

# 6) Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами
# от 10 до 310

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/digits_2.csv"

n_10_300 = list(range(10, 311))

with open(file_name, 'w') as fn:
    writer = csv.writer(fn, lineterminator='\n')
    writer.writerow(['number'])
    for i in n_10_300:
        writer.writerow([i])

# 7) Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными
# именами

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/names_2.csv"

r_n = [names.get_full_name() for i in range(400)]

with open(file_name, 'w') as fn:
    writer = csv.writer(fn, lineterminator='\n')
    writer.writerow(['name'])
    for i in r_n:
        writer.writerow([i])

# 8) Вариант 2. Создать emails_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк
# с разными имейлами что-то@gmail.com

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/emails_2.csv"

email = [names.get_first_name() + str(i) + '@gmail.com' for i in range(400)]

with open(file_name, 'w') as fn:
    writer = csv.writer(fn, lineterminator='\n')
    writer.writerow(['email'])
    for i in email:
        writer.writerow([i])

# 9) Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк.
# Имя и часть email до @ должны совпадать.

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/nne_2.csv"

Number = ['89' + str(random.randint(100000000, 999999999)) for _ in range(450)]
Name = [names.get_first_name() + str(j) for j in range(450)]
Email = [Name[i] + '@gmail.com' for i in range(450)]

with open(file_name, 'w') as fn:
    column = ['Number', 'Name', 'Email']
    writer = csv.DictWriter(fn, fieldnames=column, lineterminator='\n')
    writer.writeheader()
    for i in range(450):
        row = {'Number': Number[i], 'Name': Name[i], 'Email': Email[i]}
        writer.writerow(row)

# 10) Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем.
# Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)

file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/nne_2.csv"
with open(file_name, 'r') as fr:
    reader = csv.reader(fr)
    s = next(reader)
    data_read = []
    for i in reader:
        data_read.append(i)

with open(file_name, 'w', newline='') as fw:
    column = s + ['Date']
    writer = csv.DictWriter(fw, fieldnames=column)
    writer.writeheader()
    counter = 0
    for i in data_read:
        counter += 1
        number = i[0]
        name = i[1]
        email = i[2]
        if counter < 51:
            gen_date = rt.random_date(start=datetime.datetime(1980, 1, 1), end=datetime.datetime(1990, 12, 31),
                                      text=False, pattern='%d-%m-%Y')
        elif counter < 151:
            gen_date = rt.random_date(start=datetime.datetime(1991, 1, 1), end=datetime.datetime(2000, 12, 31),
                                      text=False, pattern='%d-%m-%Y')
        elif counter < 301:
            gen_date = rt.random_date(start=datetime.datetime(2001, 1, 1), end=datetime.datetime(2010, 12, 31),
                                      text=False, pattern='%d-%m-%Y')
        elif counter < 452:
            gen_date = rt.random_date(start=datetime.datetime(2011, 1, 1), end=datetime.datetime(2021, 12, 31),
                                      text=False, pattern='%d-%m-%Y')
        row = {column[0]: number, column[1]: name, column[2]: email, column[3]: gen_date}
        writer.writerow(row)

# Создать файл combo.csv с полями Name, Email, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

combo_file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/combo.csv"
file_name = "C:/Users\Роман\PycharmProjects\pythonProject\Python_course_Vadim_Ksendzov/nne_2.csv"

with open(file_name, 'r') as fn:
    reader = csv.DictReader(fn)
    nne_2_names = []
    nne_2_dates = []
    for i in reader:
        nne_2_names.append(i['Name'])
        nne_2_dates.append(i['Date'])

rest_nne_2_names = [names.get_first_name() for i in range(550)]

full_names = nne_2_names + rest_nne_2_names
full_names.sort()


email = [full_names[i] + '@gmail.com' for i in range(len(full_names))]
number = ['89' + str(random.randint(100000000, 999999999)) for _ in range(1000)]
gender = [random.choice(['male', 'female']) for i in range(1000)]
salary = [random.randint(30000, 210000) for i in range(1000)]


rest_nne_2_dates = []
for i in range(550):
    random_d = rt.random_date(start=datetime.datetime(2001, 1, 1), end=datetime.datetime(2010, 12, 31),
                                                text=False, pattern='%d-%m-%Y')
    rest_nne_2_dates.append(random_d.strftime('%d-%m-%Y'))

full_dates = nne_2_dates + rest_nne_2_dates

with open(combo_file_name, 'w') as cf:
    column = ['Name', 'Email', 'Date', 'Phone', 'Gender', 'Salary']
    writer = csv.DictWriter(cf, fieldnames=column, lineterminator='\n')
    writer.writeheader()
    for i in range(1000):
        row = {'Name': full_names[i], 'Email': email[i], 'Date': full_dates[i], 'Phone': number[i],
               'Gender': gender[i], 'Salary': salary[i]}
        writer.writerow(row)





