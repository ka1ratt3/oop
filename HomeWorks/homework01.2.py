class Hero:

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl


    def introduce(self):
        print(f'Привет, меня зовут {self.name}, у меня {self.hp} здоровья и {self.lvl} уровень')

    def is_adult(self):
        return self.lvl >= 10

hero1 = Hero('naofume', 70, 13)
hero2 = Hero('krasavchik', 70, 9)
hero3 = Hero('sven', 70, 11)
hero4 = Hero('yournero', 70, 5)


print(f"{hero1.name}, {hero1.is_adult()}")
print(f"{hero2.name}, {hero2.is_adult()}")
print(f"{hero3.name}, {hero3.is_adult()}")
print(f"{hero2.name}, {hero2.is_adult()}")
print(f"{hero4.name}, {hero3.is_adult()}")