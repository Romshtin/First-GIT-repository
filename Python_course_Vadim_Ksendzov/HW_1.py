string = 'Мне'
integer = 25
float_number = .10
bytes_type = bytes('Hello', 'UTF-8')
bytes_type_1 = bytes([1, 2, 5, 10, 23])
list_type = [['asdasd', 132], [True, False, 16.2]]
turple_type = (2, 5, 9, 'apples')
set_type_1 = {'Мне', 25, .10, (2, 5, 9, 'apples')}
set_type_2 = set('Hello')
set_type_3 = set({'Мне', 25, .10, (2, 5, 9, 'apples')})
frozen_set_type = frozenset('Hello')
dictionary_type = {'Roman': 25,
                   'Vera': 36,
                   'Ivan': 32
                   }
a = 'Привет '
b = 'человек'
ab = a + b
c = 7900000000

print(string, type(string))
print(integer, type(integer))
print(float_number, type(float_number))
print(bytes_type, type(bytes_type))
print(list_type, type(list_type))
print(turple_type, type(turple_type))
print(set_type_1, type(set_type_1))
print(frozen_set_type, type(frozen_set_type))
print(dictionary_type, type(dictionary_type))
print(ab)
print(ab, c)
print(a + str(c) + ' ' + b)
