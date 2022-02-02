from bs4 import BeautifulSoup
import requests
import os
os.system('pip3 install pyfiglet')
BRed="\033[1;31m" # Red
import os
os.system('pyfiglet  By_PisTolerQ')
def proxyÇekme():

    proxies = []
    link = "https://www.sslproxies.org/"
    r = requests.get(link)
    s = BeautifulSoup(r.text,"html.parser")

    for i in s.find_all("tr")[:80]:
        try:
            data = i.find_all("td")
            address = data[0].text
            port = data[1].text
            type_ = data[4].text
            proxy = address+ ":" + port
            proxies.append(proxy)
        except:
            pass
    return proxies

for proxy in proxyÇekme():
    print(BRed + proxy)
