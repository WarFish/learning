# 1. Напишите первую строку класса Poodle (Пудель).
# Этот класс должен расширять класс Dog.
class Poodle(Dog):

# 3. Взгляните на приведенное ниже определение:
# class Beverage:
#   def __init__(self, bev_name):
#       self.__bev_name = bev_name
#
# Напишите программный код класса с именем Cola (Кока-кола), который является подклассом класса
# Beverage (Напиток). Метод __init__() класс Cola должен вызывать метод __init__() класса
# Beverage, передавая строковое значение 'кока-кола' в качестве аргумента.
class Cola(Beverage):
    def __init__(self):
        Beverage.__init__(self, 'кока-кола')
