import urllib.request
import urllib.parse
import urllib.error
import socket

#urllib.request.urlopen(url,data=None,timeout,cafile,capath,
#                       cadefault,context)
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')
print(response.read())
