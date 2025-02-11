import requests

city = "Bishkek"

url = f"https://wttr.in/{city}?format=%C+%t"

response = requests.get(url)

if response.status_code == 200:
    print(f"Погода в {city}: {response.text}")
else:
    print(f"Ошибка! Код состояния: {response.status_code}")

"""Библиотека requests это инструмент для отправки
 http запросов и в следствии получения данных от этих сайтов"""

"""1: Отправка запроса
2: получения ответа
3: работа с этим самым ответом"""