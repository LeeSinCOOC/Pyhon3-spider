from urllib import request,error

try:
    response = request.urlopen('https://www.cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers)
    
#Not Found 404 Server: nginx/1.10.3 (Ubuntu)
#Date: Tue, 09 Apr 2019 13:06:13 GMT
#Content-Type: text/html; charset=UTF-8
#Transfer-Encoding: chunked
#Connection: close
#Vary: Cookie
#Expires: Wed, 11 Jan 1984 05:00:00 GMT
#Cache-Control: no-cache, must-revalidate, max-age=0
#Link: <https://cuiqingcai.com/wp-json/>; rel="https://api.w.org/"