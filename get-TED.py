import requests
from get_ip import get_random_ip
from bs4 import BeautifulSoup
import os

head = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'proxies': get_random_ip(),
    'ue': 'utf-8',
}
path = r'F:\TED'

def get_TED(url, count):
    page_part = url.split('=')
    for i in range(1, count+1):
        url_ted = page_part[0] + '=' + str(i)
        response = requests.get(url_ted, params=head)
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        talks_list = bs.find_all('div', attrs={'class': 'media__message'})
        for j in range(len(talks_list)):
            ted_a = talks_list[j].find_all('a', attrs={'class': 'ga-link', 'data-ga-context': 'talks'})
            ted_url = 'https://www.ted.com' + ted_a[0]['href']
            print("TED演讲主题：" + ted_a[0].text)
            os.system(r'you-get -o {} {}'.format(path, ted_url))

if __name__ == '__main__':
    url = 'https://www.ted.com/talks?page=1'
    count = int(input("请输入要下载的页数（一页36个TED）："))
    get_TED(url, count)