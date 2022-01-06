import requests as r
from my_token import token
import datetime


def get_weather(city, token):
    try:
        request = r.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = request.json()
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}****",
              f"Город : {data['name']}",
              f"Температура сейчас : {data['main']['temp']}",
              f"Максимальная температура в течении дня : {data['main']['temp_max']}",
              f"Минимальная температура в течении дня : {data['main']['temp_min']}",
              f"Cкорость ветра : {data['wind']['speed']} м/с",
              f"Восход солнца : {datetime.datetime.fromtimestamp(data['sys']['sunrise'])}",
              f"Закат : {datetime.datetime.fromtimestamp(data['sys']['sunset'])}",
              f"Продолжительность дня : {datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])}",
              sep='\n')
    except Exception as ex:
        print("Something_wrong")


def main():
    city = input("Введите ваш город - ")
    get_weather(city, token)


if __name__ == '__main__':
    main()
