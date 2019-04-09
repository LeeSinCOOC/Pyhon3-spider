from urllib.parse import quote,unquote #中文URL会乱码，这个可以转化为URL编码

keyword = '辣鸡'

print(quote(keyword)) 
#%E8%BE%A3%E9%B8%A1

print(unquote('%E8%BE%A3%E9%B8%A1'))
#辣鸡