# Python_2. HW_1


# 1) Создать переменную типа String
string = 'Мне'
# 2) Создать переменную типа Integer
integer = 25
# 3) Создать переменную типа Float
float_number = .10
# 4) Создать переменную типа Bytes
bytes_type_1 = b'Roman'
bytes_type_2 = bytes('Hello', 'UTF-8')
bytes_type_3 = bytes([1, 2, 5, 10, 23])
# 5) Создать переменную типа List
list_type = [['asdasd', 132], [True, False, 16.2]]
# 6) Создать переменную типа Tuple
turple_type = (2, 5, 9, 'apples')
# 7) Создать переменную типа Set
set_type_1 = {'Мне', 25, .10, (2, 5, 9, 'apples')}
set_type_2 = set('Hello')
# 8. Создать переменную типа Frozen set
frozen_set_type = frozenset('Hello')
# 9) Создать переменную типа Dict
dictionary_type = {'Roman': 25,
                   'Vera': 36,
                   'Ivan': 32
                   }
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(string, type(string))
print(integer, type(integer))
print(float_number, type(float_number))
print(bytes_type_1, type(bytes_type_1), bytes_type_2, type(bytes_type_2), bytes_type_3, type(bytes_type_3))
print(list_type, type(list_type))
print(turple_type, type(turple_type))
print(set_type_1, type(set_type_1), set_type_2, type(set_type_2))
print(frozen_set_type, type(frozen_set_type))
print(dictionary_type, type(dictionary_type))
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'Привет '
b = 'человек'
ab = a + b
print(ab)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
c = 7900000000
print(ab, c)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(a + str(c) + ' ' + b)
