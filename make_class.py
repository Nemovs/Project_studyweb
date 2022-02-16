if __name__=="__main__":

    class Robot:
        """Представляет робота с именем."""
    # Переменная класса, содержащая количество роботов
        population = 0

        def __init__(self, name):
            """Инициализация данных."""
            self.name = name
            print(f"Инициализация {self.name}")
    # При создании этой личности, робот добавляется # к переменной 'population'
            Robot.population += 1

        def __del__(self):
            """Я умираю."""
            print(f"{self.name} уничтожается!")
            Robot.population -= 1
            if Robot.population == 0:
                print(f"{self.name} был последним.")
            else:
                print(f"Осталось {Robot.population:d} работающих роботов.")

        def say_hi(self):
            """Приветствие робота. Да, они это могут."""
            print(f"Приветствую! Мои хозяева называют меня {self.name}.")

        def how_many():
            """Выводит численность роботов."""
            print(f"У нас {Robot.population:d} роботов.")
        how_many = staticmethod(how_many)


    droid1 = Robot('R2-D2')
    droid1.say_hi()
    Robot.how_many()
    droid2 = Robot('C-3PO')
    droid2.say_hi()
    Robot.how_many()
    print("\nЗдесь роботы могут проделать какую-то работу.\n")
    print("Роботы закончили свою работу. Давайте уничтожим их.")
    del droid1
    del droid2
    Robot.how_many()
