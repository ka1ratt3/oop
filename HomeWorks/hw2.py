class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} отрегенился на {self.hp} очков здоровья")

    def attack(self):
        print(f'{self.name}s attack')

gerald = Heroes('Gerald', 15)
gerald.action()
gerald.attack()


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision



