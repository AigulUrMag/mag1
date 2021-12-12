import requests
import time
from threading import Thread
from datetime import datetime
def get_html(link):
    response = requests.get(link)
    print(link, len(response.text))

urls=['https://google.ru','https://yandex.ru','https://mail.ru']
t1=time.time()
for i in urls:
    get_html(i)
print('time1',(time.time()-t1).microseconds)    

threads = [Thread(target=get_html(i), args=(i)) for i in urls]
t2=time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
print('time2',(time.time()-t2).microseconds)
