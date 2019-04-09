import requests

r = requests.get('http://www.baidu.com')
print(r.cookies)

for k,v in r.cookies.items(): # items后面有括号
    print(k+'='+v)
    
#<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
#BDORZ=27315