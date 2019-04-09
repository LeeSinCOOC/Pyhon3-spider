from urllib.parse import urlencode

data = {
        'name':'a',
        'pass':'b'}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(data)
print(url)