import requests
import os
import time
import random
from bs4 import BeautifulSoup


##设置你要下载的图片类型，默认为1风景照片，以下为备选项
number_type = 1
##你也可以设置随机值，照片随机
#list = [1, 2, 3, 7, 9, 10, 11, 12, 13, 14, 15]
#number_type = random.choice(list)

if number_type == 1 :   ##风景壁纸，number_type设置为
    url_type = "zhuomianbizhi/fengjing/"  
    t = random.randint(1,150)
    url_base = "https://www.enterdesk.com/"
elif number_type == 2 :  ##花卉壁纸，number_type设置为2
    url_type = "zhuomianbizhi/huahui/"
    t = random.randint(1,58)
    url_base = "https://www.enterdesk.com/"
elif number_type == 3 :  ##人文壁纸，number_type设置为3
    url_type = "zhuomianbizhi/renwenbizhi/"
    t = random.randint(1,26)
    url_base = "https://www.enterdesk.com/"
elif number_type == 4 :  ##汽车壁纸，number_type设置为4
    url_type = "zhuomianbizhi/qichebizhi/"
    t = random.randint(1,43)
elif number_type == 5 :  ##影视壁纸，number_type设置为5
    url_type = "zhuomianbizhi/yingshibizhi/"
    t = random.randint(1,66)
    url_base = "https://www.enterdesk.com/"
elif number_type == 6 :  ##明星壁纸，number_type设置为6
    url_type = "zhuomianbizhi/mingxingbizhi/"
    t = random.randint(1,109)
    url_base = "https://www.enterdesk.com/"
elif number_type == 7 :  ##摄影壁纸，number_type设置为7
    url_type = "zhuomianbizhi/sheying/"
    t = random.randint(1,47)
    url_base = "https://www.enterdesk.com/"
elif number_type == 8 :  ##美食壁纸，number_type设置为8
    url_type = "zhuomianbizhi/meishibizhi/"
    t = random.randint(1,13)
    url_base = "https://www.enterdesk.com/"
elif number_type == 9 :  ##动漫壁纸，number_type设置为9
    url_type = "dongmanmeinv/"
    t = random.randint(1,5)
    url_base = "https://mm.enterdesk.com/"
elif number_type == 10 :  ##大陆美女壁纸，number_type设置为10
    url_type = "dalumeinv/"
    t = random.randint(1,97)
    url_base = "https://mm.enterdesk.com/"
elif number_type == 11 :  ##日韩美女壁纸，number_type设置为11
    url_type = "rihanmeinv/"
    t = random.randint(1,15)
    url_base = "https://mm.enterdesk.com/"
elif number_type == 12 :  ##港台美女壁纸，number_type设置为12
    url_type = "gangtaimeinv/"
    t = random.randint(1,6)
    url_base = "https://mm.enterdesk.com/"
elif number_type == 13 :  ##清纯美女壁纸，number_type设置为13
    url_type = "qingchunmeinv/"
    t = random.randint(1,38)
    url_base = "https://mm.enterdesk.com/"
elif number_type == 14 :  ##可爱美女壁纸，number_type设置为14
    url_type = "keaimeinv/"
    t = random.randint(1,10)
    url_base = "https://mm.enterdesk.com/"
elif number_type == 15 :  ##欧美美女壁纸，number_type设置为15
    url_type = "oumeimeinv/"
    t = random.randint(1,26)
    url_base = "https://mm.enterdesk.com/"
else:
    exit()

url_t_1 = str(t)
url_t_2 = ".html"
url = url_base + url_type + url_t_1 + url_t_2


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
                    with open('/opt/python_pic/python_jpg/tupian.jpg', 'wb') as f:
                        f.write(img)
                    time.sleep(600)
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



