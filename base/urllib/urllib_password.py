from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username ='a'
password = 'b'
url = 'http://loachost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auto_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auto_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')  
    print(html)
except URLError as e:
    print(e.reason)
    