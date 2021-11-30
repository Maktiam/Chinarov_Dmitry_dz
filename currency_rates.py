import requests
from datetime import date

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(currency):
    found = False
    html = requests.get(url).text
    datehtml = html[html.find('Date=') + 6:html.find('Date=') + 16]
    datehtml = datehtml.split('.')
    date_currency = date(int(datehtml[2]), int(datehtml[1]), int(datehtml[0]))
    for el in html.split('<Valute ID="')[1:]:
        if currency.upper() in el[el.find('<CharCode>') + 10:el.find('</CharCode>')]:
            found = True
            name = el[el.find('<Name>') + 6:el.find('</Name>')]
            nominal = float(el[el.find('<Nominal>') + 9:el.find('</Nominal>')])
            value = el[el.find('<Value>') + 7:el.find('</Value>')]
            value = float(value.replace(',', '.'))

            print('Курс на ' + str(date_currency) + ' ' + name + ':' + str(value / nominal))
            break
    if found == False:
        print('Валюта ' + currency +  ' не найдена.')


if __name__ == '__main__':
    currency_rates('usd')
    currency_rates('eur')
    