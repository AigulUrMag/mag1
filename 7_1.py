from bs4 import BeautifulSoup
import requests

url="http://mfd.ru/currency/?currency=USD"
page = requests.get(url)
print(page.status_code)
Dollars_rubl = []
Kurs = []
soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
Kurs = soup.findAll(class_="mfd-table mfd-currency-table")
for data in Kurs:
    if data.find_all(class_="m-chart-v") is not None:
        Dollars_rubl.append(data.text)
for data in Dollars_rubl:
    print(data)        