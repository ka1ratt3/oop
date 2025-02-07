# """Абстракция"""
# from abc import ABC, abstractmethod
#
# import random
#
#
#
# class OTPService(ABC):
#     @abstractmethod
#     def sms_send(self):
#         pass
#
#
#
#
# class NikitaOTP(OTPService):
#
#     def sms_send(self, phone):
#         phone = input("Введите тел в формате +996")
#
#
# class TwilioOTP(OTPService):
#
#     def sms_send(self, phone):
#         phone = input("Введите тел в формате +7xxx xx xx xx xx")
#
#
# class Animal(ABC):
#
#     # Декоратор
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     def move(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return print('Gaf Gaf')
#
#     def move(self):
#         return print('Run')
# dog = Dog()
#
# dog.make_sound()
# dog.move()




"""Модули"""

from colorama import Fore, Back, Style



from colorama import Fore, Back, Style



print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')