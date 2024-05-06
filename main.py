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

time_since = "2024"

proxies = {
    "http": "http://localhost:7890",
    "https": "http://localhost:7890",
}
headers = {}
# headers =  {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "priority": "u=0, i",
#     "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
#     "sec-ch-ua-arch": "\"x86\"",
#     "sec-ch-ua-bitness": "\"64\"",
#     "sec-ch-ua-full-version-list": "\"Chromium\";v=\"124.0.6367.61\", \"Microsoft Edge\";v=\"124.0.2478.51\", \"Not-A.Brand\";v=\"99.0.0.0\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-model": "\"\"",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-ch-ua-platform-version": "\"15.0.0\"",
#     "sec-ch-ua-wow64": "?0",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "cookie": "HSID=AcA2TzkF8-7frcvu7; SSID=AiuFo92cjlgDj_Aid; APISID=yjyo8Lp-KgmfhJb0/AQXHDY_IL27N7lrWt; SAPISID=hR8eCx7FhRM3w3q4/AiZTZYexdx5J_u5Y1; __Secure-1PAPISID=hR8eCx7FhRM3w3q4/AiZTZYexdx5J_u5Y1; __Secure-3PAPISID=hR8eCx7FhRM3w3q4/AiZTZYexdx5J_u5Y1; SID=g.a000hwjL31WjbuMMoHDb8ZUG95cObH05lh_ll8Fz4J_OCdcwvLeRVacxQC-WDtHlkKF5oAeKiAACgYKAdMSAQASFQHGX2MiiHaWHOFWhvxBSIYzla8fGxoVAUF8yKqqIeY64N2iDOLU_bPbOALe0076; __Secure-1PSID=g.a000hwjL31WjbuMMoHDb8ZUG95cObH05lh_ll8Fz4J_OCdcwvLeRIr0hmZYNrLlnwjkOS1iofgACgYKAasSAQASFQHGX2Mi71cttLC2FuskvZhj2hw3FRoVAUF8yKp6SQ_uA016NjlsvQOw0C2v0076; __Secure-3PSID=g.a000hwjL31WjbuMMoHDb8ZUG95cObH05lh_ll8Fz4J_OCdcwvLeRikhfFX8f9hpN3S1dRci3EAACgYKARcSAQASFQHGX2Mi-aoqqTm8NcgUfbgCjuFj9xoVAUF8yKoFsQ56BNdx6Rz6Bmb_OLBE0076; GSP=IN=7e6cc990821af63:LD=zh-CN:LR=lang_en|lang_ja:A=DweFnQ:CPTS=1695882097:LM=1712832110:S=38bzY7vDNauFzE2G; AEC=AQTF6Hyr6uZ0IDHrzCLtBDwciHP-v43Qd-cSv3CsTcgqP4LyHAuWko3GFg; 1P_JAR=2024-04-22-02; __Secure-1PSIDTS=sidts-CjEB7F1E_EBXk6pNGxiYHCptvUCpJUnws8LzQk7JunXJ-8YPE2lWafyYtJp4ofh5nu-1EAA; __Secure-3PSIDTS=sidts-CjEB7F1E_EBXk6pNGxiYHCptvUCpJUnws8LzQk7JunXJ-8YPE2lWafyYtJp4ofh5nu-1EAA; NID=513=ZzibWnjSSxgq4ohReaU7FHcVqQ_zbAJuzR_iifDvz7D702f0sd3bpjMiF-PeEl3KpVpdZqpziR0b0nQ4e4CaNfvL92CNDuzfVovwpygyXFnF0Y_jJEC4dpfD4K7fwKDPYtv9SS8_Ocr0SYuyDd4cqVPi0MDmgeAazGkUvQShsl0VE6Tf3gcMDmUEUvfbZ8l6MmDwssTRfyXSnYTuLjZ3dleNEJ1ohmQZLVQjBoWbtS3UIzor4I4tDDBgiD-TquqtEc1bVWLx-iVvDnqqeNngr0Vh1yQ2FVFrj9sQxJtJLpIHF9bNXY62bL7QSiNaxCT-hVO-O4_o5kzbwoQgoBbVXaSFxv-J3euCnWQ; SIDCC=AKEyXzUm83AZS6RWtmdQdJGwCGUeev0Zz3ELvsV1B3RQ445v51zfahH4gUlhBmscbPAit3mtpQ; __Secure-1PSIDCC=AKEyXzW_uEMeKoB6veiRLIDQBpNu1P_Uiapvo8pbwTdfBP3W0tRAHfDntnbmkUisWoMAWILtyQ; __Secure-3PSIDCC=AKEyXzXnxA7nf8gHXQmGd4bpEh6azpPs8tMp1CEzJL_SskgtUyP9dVUszW_IctxX7Gxg7FuG8dQ",
#     "Referer": "https://scholar.google.com/",
#     "Referrer-Policy": "origin-when-cross-origin"
#   }

download_directory = target_file[ : -(len(re.findall('/[^/]*\.txt',target_file)[0]) - 1)]

with open(target_file,'r',encoding = 'utf-8') as f:
    target_text = f.read()
    title_list = re.split('\n',target_text)

def download(title:str, idx:int):

    word_list = re.split('\s',title)

    q = ''
    
    for i in range(len(word_list)):
        if(i==0):
            q += word_list[i]
        else:
            q += '+' + word_list[i]

    url = 'https://scholar.google.com/scholar?' + 'as_ylo' + time_since + '&q=' + q

    res = requests.get(url = url, proxies = proxies, verify= False, headers=headers)

    try:
        soup = BeautifulSoup(res.text,'html.parser')
        url_item = soup.find('div',class_="gs_or_ggsm")
        a_item = url_item.find('a')
        url = a_item.get('href')
        print('find url: ',url)
    except:
        print('cant find url for ',title)
        title_list[idx] = 'cant find url for ' + title
        return

    try:
        response = requests.get(url,  proxies = proxies, verify= False)
    except:
        print('request error')
        title_list[idx] = 'request error' + title
        return 'request error'
    
    replace_list =['<','>','/','\\','|',':','"','*','?']
    for char in replace_list:
        title = title.replace(char,'')
    print('title: ',title)


    open(download_directory + title + '.pdf' ,'wb').write(response.content)


    print('complete ' + title)
    title_list[idx] = 'complete ' + title
    return 'complete ' + title


threads = []


for i, service in enumerate(title_list):
    thread = threading.Thread(target=download, kwargs={"title": title_list[i], "idx" : i})
    threads.append(thread)

# 启动线程
for i in range(len(threads)):
    threads[i].start()
    time.sleep(5)

for i in range(len(threads)):
    threads[i].join()

result_text = '\n'.join(title_list)

with open(download_directory + '\\result.txt', mode='w',encoding = 'utf-8') as f:
    f.write(result_text)


