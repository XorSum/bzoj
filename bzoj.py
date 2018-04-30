# coding: UTF-8
import time

import requests
import codecs

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
           "Accept-Encoding": "gzip",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
           }
encoding = "utf-8"
folder = "C:\\Users\\han\\Documents\\bzoj\\"

purl = "https://www.lydsy.com/JudgeOnline/problem.php"

for pid in range(1000,1500):
    payload = {"id":pid}
    r = requests.get(purl,params=payload,headers=headers)
    print(r.url,r.status_code)
    content = r.content.decode(encoding)
    filename = folder + str(pid) + ".html"
    with codecs.open(filename, "w", "utf-8") as f:
        f.write(content)
        f.close()
    time.sleep(0.1)


