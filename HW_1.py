string = 'Мне'
integer = 25
float_number = .10
Bytes = bytes('Hello', 'UTF-8')
List = [['asdasd', 132], [True, False, 16.2]]
Turple = (2, 5, 9, 'apples')
Set1 = {'Мне', 25, .10, (2, 5, 9, 'apples')}
Set2 = set('Hello')
Set3 = set(['Мне', 25, .10, (2, 5, 9, 'apples')])
Frozen_set = frozenset('Hello')
Dictionary = {'Roman': 25,
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
print(Bytes, type(Bytes))
print(List, type(list))
print(Turple, type(Turple))
print(Set1, type(Set1))
print(Frozen_set, type(Frozen_set))
print(Dictionary, type(Dictionary))
print(ab)
print(ab, c)
print(a + str(c) + ' ' + b)
