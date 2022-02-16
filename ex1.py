import ast
while True:
    try:
        def first():
            x = ast.literal_eval((input('Введите число:', )))
            x //= 2
            return x
        x = first()

        def sec(x):
            x *= 4
            return x
        print(sec(x))
        print()
        print('Теперь еще раз')
    except ValueError:
        print('Хуйню ввели, вводите цифры')







'''while True:
    x = ast.literal_eval((input('Введите число:', )))
    y = ast.literal_eval((input('Введите число:', )))
    z = x % y
    def toFixed(z, digits=0): # функция для ограничения кол-ва знаков после запятой
        return f"{z:.{digits}f}"
    print(f"переменная х типа: {type(x)}")
    print(f"переменная y типа: {type(y)}")
    print(f"остаток от деления {x} на {y} составляет {toFixed(z, 2)}")'''