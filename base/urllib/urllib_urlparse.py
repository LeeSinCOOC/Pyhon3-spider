from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result) 

print(result.scheme,result[0]) #http http 是元组              

#<class 'urllib.parse.ParseResult'> 
#ParseResult(scheme='http', netloc='www.baidu.com', 
#            path='/index.html', params='user', query='id=5', 
#            fragment='comment')