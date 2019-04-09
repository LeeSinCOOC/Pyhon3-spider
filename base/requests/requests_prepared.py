from requests import Request,Session

url = 'http://httpbin.org/post'

data = {
        'name':'a',
        'pass':'b'}
s = Session()
req = Request('POST',url,data=data)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

#建立Request对象，在进行队列调度时会非常方便