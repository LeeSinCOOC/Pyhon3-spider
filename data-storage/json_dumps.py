import json

string = '''
[{
"name":"bob",
"gender":"m",
"age":"13"},
{
"name":"王王",
"gender":"w",
"age":"14"}]
'''
print(type(string))

jso = json.loads(string) #加s
print(type(jso))

data = json.dumps(jso,indent=2,ensure_ascii=False) #indent保留缩进，ensure_ascii改为False确保中文字符正常，写的时候也可以添加字符编码utf8
with open('json.json','w') as f:
    f.write(data)