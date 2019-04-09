#urllib
#    1.request
#    2.error
#    3.parse
#    4.robotparser

#1.urlopen()
import urllib.request

response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode('utf-8'))
print(type(response)) #<class 'http.client.HTTPResponse'>

#HTTPResponse包含了：read() readinto() getheader(name) getheaders()
#                    fileno()方法
#msg version status reason debuglevel closed 属性