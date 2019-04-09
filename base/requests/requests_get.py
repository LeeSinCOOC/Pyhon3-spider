import requests

url = 'http://www.httpbin.org/get'
data = {
        'name':'a',
        'pass':'b'}

r = requests.get(url,params=data)

print(type(r))
print(r.status_code)
print(r.text)
print(r.cookies)

print(r.json()) 

#text 返回字符串 如果要返回字典直接用json()注意有括号