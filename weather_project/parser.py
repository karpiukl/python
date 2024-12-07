from bs4 import BeautifulSoup

def parse_weather_data(html: str):
    """
    Розбирає дані про погоду з HTML-контенту.

    :param html: HTML-контент у вигляді рядка
    :return: Список температур на сьогодні
    """
    soup = BeautifulSoup(html, 'html.parser')
    temperatures = soup.find_all('p', class_='today-temp')
    return [temp.text for temp in temperatures]
