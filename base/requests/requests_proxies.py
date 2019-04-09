import requests

proxies = {
        'http':'http://10.10.1.1:2222',
        'http':'http://10.10.1.2:3333'}
requests.get('http://www.taobao.com',proxies=proxies)