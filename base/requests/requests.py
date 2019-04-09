import requests

url = 'http://www.baidu.com'

r = requests.get(url)

print(type(r))
print(r.status_code)
print(r.text)
print(r.cookies)