import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://www.taobao.com',auth=HTTPBasicAuth(
        'username','password'))

#也可以直接传元组，因为默认就使用这个类
r = requests.get('http://www.taobao.com',auth=('username','password'))

