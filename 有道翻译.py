import requests
import json

content = input("输入需要翻译的内容：")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1522826491064',
    'sign': '43423b06d74defd484186ff32ebffae8',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'true',
    'ue': 'UTF-8'#设置翻译支持中文
}

response = requests.get(url, params=header)
response.encoding = 'utf-8'
html = response.text

trans = json.loads(html)
# print(type(trans), trans)
print('')
print("翻译结果：")
print(trans['translateResult'][0][0]['tgt'])