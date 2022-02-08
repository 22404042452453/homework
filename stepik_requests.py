"""Мы сохранили страницу с википедии про языки программирования и сохранили по адресу https://stepik.org/media/attachments/lesson/209717/1.html

Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ должен быть одной из этих двух строк).
"""

import requests

url = "https://stepik.org/media/attachments/lesson/209717/1.html"

if requests.get(url).status_code:
    response = requests.get(url)
    if str(response.content).count("C++") > str(response.content).count("Python"):
        print("C++")
    else:
        print("Python")
else:
    print("Ups_something_wrong")
