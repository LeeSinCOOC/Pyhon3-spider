import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
r = requests.get('http://www.baidu.com',headers=headers)
print(r.text)

data = {
        'name':'a',
        'pass':'b'}

pos = requests.post('http://httpbin.org/post',data=data)
print(pos.text)