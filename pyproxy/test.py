# coding: utf8 
import sys
import requests


url = 'https://www.cnblogs.com/dzqdzq/p/9822187.html'
proxies = {'http': 'http://localhost:8899', 
        'https': 'http://localhost:8899'}
r = requests.get(url, proxies=proxies)
print(r.status_code)
print(len(r.content))

