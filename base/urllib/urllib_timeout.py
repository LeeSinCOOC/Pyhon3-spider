import urllib.request
import urllib.parse

#urllib.request.urlopen(url,data=None,timeout,cafile,capath,
#                       cadefault,context)
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
print(response.read())
