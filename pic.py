import requests
import os
import time
from bs4 import BeautifulSoup
##网址
url = "https://www.enterdesk.com/zhuomianbizhi/fengjing/"
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
                    with open('/opt/python_pic/python_jpg/1/tupian.jpg', 'wb') as f:
                        f.write(img)
                except:
                    print("爬取错误")
                    exit()
            except:
                print("爬取错误")
                exit()
    exit()
                
except:
    print("爬取错误")
    exit()



