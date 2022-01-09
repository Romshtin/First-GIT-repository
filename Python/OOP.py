class Car:
    color = 'red'
    form = 'sedan'
    engine = '3'
    speed = 100

    def move(self, impuls):
        self.speed = impuls

    def changecolor(self, paint):
        self.color = paint


obj1 = Car()
obj2 = Car()

print('OBJ1', obj1.speed, obj1.color, obj1.form, obj1.engine)
print('OBJ2', obj2.speed, obj2.color, obj2.form, obj2.engine)

obj1.move(50)
obj1.changecolor('blue')
print('OBJ1 new speed =', obj1.speed, 'OBJ1 new color =', obj1.color)

obj2.move(70)
obj2.changecolor('black')
print('OBJ2 new speed =', obj2.speed, 'OBJ2 new color =', obj2.color)

class No_init_Car:

    def car_actionts(self, act_1, act_2):
        self.a_move = act_1
        self.a_stop = act_2


car_1 = No_init_Car()  # создание экземпляра класса
car_1.car_actionts('Move', 'Stop')
print('Car_1', car_1.a_move, car_1.a_stop)

car_2 = No_init_Car()
car_2.car_actionts('Fly', 'Swim')
print('Car_2', car_2.a_move, car_2.a_stop)


class Track:
    def __init__(self, act_1, act_2):  # конструктор
        self.a_move = act_1
        self.a_stop = act_2


track_1 = Track('Drive', 'Chill')
print(track_1.a_move, track_1.a_stop)

track_2 = Track('Fly', 'Eat')
print(track_2.a_move, track_2.a_stop)


class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('display_count', Employee.emp_count)

    def display_name_salary(self):
        print('display_name_salary', self.name, self.salary)


employee_1 = Employee('Roman', 50000)

employee_1.display_name_salary()
employee_1.display_count()

employee_2 = Employee('Zoya', 45000)

employee_2.display_name_salary()
employee_2.display_count()


def ii(cl_ex, params_list, ch):

    count = 0


    for i in params_list:
        param_value = count

        if i == 'Children':
            setattr(cl_ex, i, ch)
            continue
        setattr(cl_ex, i, param_value)
        count += 1

employee_1 = Employee('Roman', 50000)
params_l = ['Children', 'Pets', 'Cars']

ii(employee_1, params_l, 2)

print('emp_1 Name =', employee_1.name)
print('emp_1 Salary =', employee_1.salary)
print('children =', employee_1.Children)
print('pets =', employee_1.Pets)
print('cars =', employee_1.Cars)

print(hasattr(employee_1, 'Cars'))

delattr(employee_1, 'Cars')
print(hasattr(employee_1, 'Cars'))


print(Employee.emp_count)
employee_1.age = 20
print('emp_1 Name', employee_1.name, 'emp_1 Age', employee_1.age, 'emp_1 Salary', employee_1.salary)

