import requests
import re
import sys
import threading
import time
from bs4 import BeautifulSoup
import warnings
 
warnings.filterwarnings('ignore')

target_file = sys.argv[1]
# target_file = './1.txt'
target_file = target_file.replace('\\','/')

proxies = {
    "http": "http://localhost:7890",
    "https": "http://localhost:7890",
}

download_directory = target_file[ : -(len(re.findall('/[^/]*\.txt',target_file)[0]) - 1)]

with open(target_file,'r',encoding = 'utf-8') as f:
    target_text = f.read()
    title_list = re.split('\n',target_text)

def download(title:str):

    word_list = re.split('\s',title)

    q = ''
    
    for i in range(len(word_list)):
        if(i==0):
            q += word_list[i]
        else:
            q += '+' + word_list[i]

    url = 'https://scholar.google.com/scholar?q=' + q

    res = requests.get(url = url, proxies = proxies, verify= False)

    try:
        soup = BeautifulSoup(res.text,'html.parser')
        url_item = soup.find('div',class_="gs_or_ggsm")
        a_item = url_item.find('a')
        url = a_item.get('href')
        print('find url: ',url)
    except:
        print('cant find url for ',title)
        return

    try:
        response = requests.get(url,  proxies = proxies, verify= False)
    except:
        print('request error')
        return 'request error'
    
    replace_list =['<','>','/','\\','|',':','"','*','?']
    for char in replace_list:
        title = title.replace(char,'')
    print('title: ',title)


    open(download_directory + title + '.pdf' ,'wb').write(response.content)


    print('complete ' + title)
    return 'complete ' + title


threads = []


for i, service in enumerate(title_list):
    thread = threading.Thread(target=download, kwargs={"title": title_list[i]})
    threads.append(thread)

# 启动线程
for i in range(len(threads)):
    threads[i].start()
    time.sleep(5)

