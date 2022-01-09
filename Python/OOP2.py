class Animan:
    def make_a_sound(self):
        print('AAAUUUFFF!!!')



class Cat(Animan):
    def tgdk(self):
        print('Tgdk-tgdk-tgdk')

    def make_a_sound(self):
        print('Meow Meow')  # Переопределение


class Dog(Animan):
    def run(self):
        print('Run-run-run')

    def make_a_sound(self):
        print('GAF-GAF')


sharik = Dog()
murzik = Cat()

sharik.make_a_sound()
murzik.make_a_sound()


class Table():
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


t1 = DeskTable(1.5, 0.8, 1.5)
print(t1.square())

class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor


t2 = ComputerTable(1.5, 0.8, 1.5)
print(t2.square(0.4))


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p

    def params(self):
        print('length', self.length)
        print('width', self.width)
        print('height', self.height)
        print('places', self.places)


class KitchenTable2(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p

    def params(self):
        print('length', self.length)
        print('width', self.width)
        print('height', self.height)
        print('places', self.places)


t3 = KitchenTable(1.5, 0.8, 1.5, 5)
t4 = KitchenTable2(1.5, 0.8, 1.5, 3)

t3.params()
t4.params()