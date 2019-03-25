##Супер скрипт который ищет что-то где-то

from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_update_time(html):
    soup = BeautifulSoup(html, 'lxml')
    updTime = soup.find('div', class_="footer-market__stat-line")
    return updTime.text

def get_comp_category(html):
    soup = BeautifulSoup(html, 'lxml')
    for t in soup.find_all('span'):
        print(t)
if __name__ == "__main__":
    html = get_html("https://market.yandex.ru/")
    if html:
        get_comp_category(html)


