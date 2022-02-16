
class Shape:
    def __init__(self, l, w):
        self.lenght = l
        self.widht = w

    def what_am_i(self):
        print(f"Я - {self.name}")

    def calculate_perimetr(self):
        return self.lenght*2+self.widht*2

class Rectangle(Shape):
    def __init__(self, l, w, name):
        Shape.__init__(self, l, w)
        self.name = name



class Square(Shape):
    def __init__(self, l, w, name):
        Shape.__init__(self, l, w)
        self.widht = self.lenght
        self.name = name

    def change_size(self, s):
        self.lenght = self.lenght+s






rectangle = Rectangle(5, 7, 'Прямоугольник')
square = Square(4, 4, 'Ебучий квадрат')
square.what_am_i()
rectangle.what_am_i()
print(square.calculate_perimetr())





'''class Circle():
    def __init__(self, pi, r):
        self.pi = pi
        self.radius = r

    def area(self):
        def toFixed(x, digits=0): # функция для ограничения кол-ва знаков после запятой
            return f"{x:.{digits}f}"
        x = self.pi * (self.radius ^ 2)
        return (toFixed(x,3))

circle = Circle(math.pi, 10)
x = circle.area()
print(x)

def toFixed(x, digits=0):
    return f"{x:.{digits}f}"

print(toFixed(x,2))

class Apple():
    def __init__(self, col, w, o, con):
        self.color = col
        self.weight = w
        self.old = o
        self.country = con
        print('Создано!')

apple = Apple('green', 250, 10, 'Canada')
x = dir(apple)
for i in x:
    if '__' not in i:
        print(f"{i}: {getattr(apple, i)}")'''