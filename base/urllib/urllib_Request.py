from urllib import request,parse

url = 'http://www.httpbin.org/post'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        ,'Host':'httpbin.org'}
dict = {
        'name':'haha'}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=headers,method='post')
response = request.urlopen(req)
print(response.read().decode('utf-8'))