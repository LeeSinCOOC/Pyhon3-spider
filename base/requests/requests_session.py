import requests

requests.get('http://httpbin.org/cookies/set/number/123456')

r = requests.get('http://httpbin.org/cookies')
print(r.text)
#{
#  "cookies": {}
#}

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/1234567')
rr = s.get('http://httpbin.org/cookies')
print(rr.text)

