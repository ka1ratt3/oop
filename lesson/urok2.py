# Полиморфизм
# class Hero:
#     def __init__(self, name, hp, lvl):
#         self.name = name
#         self.hp = hp
#         self.lvl = lvl
#
#     def action(self):
#         print(f"base action")
#
# class Warrior(Hero):
#
#
#     def __init__(self,name='John Doe', hp=100, lvl=1, st=50):
#         super().__init__(name, hp, lvl)
#         self.st = st
#         self.name = name
#         self.hp = hp
#         self.lvl = lvl
#     def action(self):
#         print(f"{self.name}, Kirrito action ")
#
#     def about_us(self):
#         print(f"NAME: {self.name} \n HP:{self.hp}")
#
# kirrito = Warrior(lvl=5, hp=1000, st=100, name='Kirrito')
# kirrito.action()
# kirrito.about_us()

# Инкапсуляция

class BankAccount:

    def __init__(self, client, balance, password):
        self.client = client # Открытый
        self._balance = balance # Защищённый атрибут
        self.__password = password # Приватный атрибут

    def about(self):
        print(f"PS: {self.__password}")

client = BankAccount("John Doe", 1000, 12345678)
# print(client._balance)
# print(client.__password)
# client.about()
print(client._BankAccount__password)
print(dir(client))