import requests
from bs4 import BeautifulSoup
import random

head = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'ue': 'utf-8',
}

def get_ip_list():
    url = 'http://www.xicidaili.com/nn/'
    response = requests.get(url, headers=head).text
    bs = BeautifulSoup(response, 'html.parser')
    ips = bs.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip():
    ips_list = get_ip_list()
    proxy_list = []
    for ip in ips_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies