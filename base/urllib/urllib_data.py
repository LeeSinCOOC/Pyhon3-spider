import urllib.request
import urllib.parse

#urllib.request.urlopen(url,data=None,timeout,cafile,capath,
#                       cadefault,context)
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())
