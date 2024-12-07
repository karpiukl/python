import requests

def fetch_weather_data(url: str) -> str:
    """
    Отримує HTML-контент за заданою URL-адресою.

    :param url: URL-адреса веб-сторінки для отримання
    :return: HTML-контент сторінки
    """
    response = requests.get(url)
    response.raise_for_status()  # Піднімає помилку при невдалому запиті
    return response.text
