from urllib.parse import urlunparse #长度必须为6 如果是split 长度必须是5 

data = ['http','www.baidu.com','index.html','user','a=6','comment']

print(urlunparse(data))
#http://www.baidu.com/index.html;user?a=6#comment 