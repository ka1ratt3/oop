class Hero:

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl


    def introduce(self):
        print(f'Привет, меня зовут {self.name}, у меня {self.hp} здоровья и {self.lvl} уровень')
hero1 = Hero('naofume', 70, 13)

hero1.introduce()