import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
from datetime import datetime #подключаем функцию для преобразования дат в нужный формат.
#matplotlib inline


url="http://mfd.ru/currency/?currency=USD"
page = requests.get(url)
Dollars_rubl = []
Kurs = []
x=[]
y=[]
y1=[]
soup = BeautifulSoup(page.text, "html.parser")
Kurs = soup.findAll(class_="mfd-table mfd-currency-table")
for data in Kurs:
    if data.find_all('span',class_="m-chart-legend-value") is not None:
        Dollars_rubl.append(data.text)
Gr_1=""
Gr_2=""        
for data in Dollars_rubl:
    Gr_1+=str(data)
Gr_2=Gr_1.split()
len1=len(Gr_2)   
for i in range(len1-1,3,-4):
    x.append(str(Gr_2[i-2]))
    print(x)
    y.append(float(str(Gr_2[i-1])))
   
flg,ax=plt.subplots()

ax.plot(x,y);
ax.set(title='Курс доллара к рублю',xlabel='Дата',ylabel='Курс')
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.grid(True)
plt.show()