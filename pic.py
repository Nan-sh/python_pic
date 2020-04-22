import requests
import os
import time
import random
from bs4 import BeautifulSoup
##网址
url_base = "https://www.enterdesk.com/zhuomianbizhi/fengjing/"
t = random.randint(1,150)
url_t_1 = str(t)
url_t_2 = ".html"
url = url_base + url_t_1 + url_t_2
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    
    soup = BeautifulSoup(r.text, "html.parser")
    dd = soup.find_all('dd')
    for temp in dd:
            temp = temp.a.attrs['href']
            temp = temp.replace('bizhi', 'download')
            url_temp = temp.replace('.html', '')
            try:
                r_temp = requests.get(url_temp)
                r_temp.raise_for_status()
                r_temp.encoding = r_temp.apparent_encoding
                soup_temp = BeautifulSoup(r_temp.text, "html.parser")
                url_download = soup_temp.img['src']
                try:
                    pic = requests.get(url_download)
                    pic.raise_for_status()
                    img = pic.content
                    with open('/opt/python_pic/python_jpg/1/tupian.jpg', 'wb') as f:
                        f.write(img)
                    time.sleep(600)
                    with open('/opt/python_pic/python_jpg/2/tupian.jpg', 'wb') as f:
                        f.write(img)
                except:
                    print("爬取错误")
                    exit()
            except:
                print("爬取错误")
                exit()
    del dd
    exit()
                
except:
    print("爬取错误")
    exit()



