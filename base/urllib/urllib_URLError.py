from urllib import request,error

try:
    request.urlopen('https://www.chenjianaaa1.com/index')
except error.URLError as e:
    print(e.reason)
    