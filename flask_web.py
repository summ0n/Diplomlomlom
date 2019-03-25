from flask import Flask, render_template
from weather import weather_by_city
from bs4 import BeautifulSoup
from requestsHTML import get_html, get_update_time


app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Moscow,Russia')
    html_base = get_html("https://market.yandex.ru/")
    if html_base:
        update_time = get_update_time(html_base)
    else:
        update_time = "Не удалось получить время последнего обновления"
    return render_template('index.html', weather=weather, ym=update_time)

if __name__ == '__main__':
    app.run(debug=True)
#@app.route('/update')
#def func02():
#    html = get_html("https://market.yandex.ru/")
#    if html:
#        tt = get_category(html)
#        return f"Test: {tt}"
#    else:
#        return 'Не обновлено'


#test = get_category(html)
#if html:
#    print(test)