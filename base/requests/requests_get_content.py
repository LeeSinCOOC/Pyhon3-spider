import requests

r = requests.get('http://github.com/favicon.ico')

print(r.text)
print(r.content)

with open('favicon.ico','wb') as f:
    f.write(r.content)