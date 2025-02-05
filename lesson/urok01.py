# ООП, GIT
# class = классовая функция (def)
class Person:
    # Это функция конструктор
    def __init__(self, name, age):
        # Атрибуты класса
        self.name = name
        self.age = age
    # Метод класса
    def introduce(self,):
        print(f"hi i'm {self.name}")

# class OBJ = Экземпляр класса
# ardager = Person('Ardager', '20')
# ardager.introduce()

# print(type(ardager))
# print(type(123))
# print(type('Hello'))


class Hero:

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl


    def introduce(self):
        print(f'Привет, меня зовут {self.name}, у меня {self.hp} здоровья и {self.lvl} уровень')

naofume = Hero("NaoFume", 100, 30)
# Дочерний класс
class ShiledHero(Hero):
    pass

naofume = ShiledHero("NaoFume", 100, 30)
naofume.action()


# class -- CamelCase
# переменные, методы, функции -- snake_case