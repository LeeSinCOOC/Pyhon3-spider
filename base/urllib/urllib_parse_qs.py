from urllib.parse import parse_qs,parse_qsl

data = 'name=a&pass=b'

print(parse_qs(data))

#{'name': ['a'], 'pass': ['b']}

print(parse_qsl(data))