from fetcher import fetch_weather_data
from parser import parse_weather_data

def get_weather(url: str):
    """
    Отримує та розбирає дані про погоду за заданою URL-адресою.

    :param url: URL-адреса веб-сайту з прогнозом погоди
    :return: Список температур на сьогодні
    """
    html = fetch_weather_data(url)
    temperatures = parse_weather_data(html)
    print("Температура на сьогодні:")
    for temp in temperatures:
        print(f" - {temp}")

def main():
    """
    Головна функція для виконання скрипта отримання погоди.
    """
    url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%83%D1%86%D1%8C%D0%BA'
    get_weather(url)

if __name__ == '__main__':
    main()
