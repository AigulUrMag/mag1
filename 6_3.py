import requests
import time
from threading import Thread
from datetime import datetime
def get_html(link):
    response = requests.get(link)
    print(link, len(response.text))

urls=['https://google.ru','https://yandex.ru','https://mail.ru']
t1=datetime.now()
for i in urls:
    get_html(i)
print('time1',(datetime.now()-t1).microseconds)    
print(time.clock())

t2=datetime.now()
threads = [Thread(target=get_html(i), args=(i)) for i in urls]
for t in threads:
    t.start()
for t in threads:
    t.join()
print('time2',(datetime.now()-t2).microseconds) 
print(time.clock())
