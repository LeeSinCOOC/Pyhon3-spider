import json

string = '''
[{
"name":"bob",
"gender":"m",
"age":"13"},
{
"name":"mary",
"gender":"w",
"age":"14"}]
'''
print(type(string))

jso = json.loads(string) #加s
print(type(jso))

print(jso[0]['name'])
print(jso[0].get('name'))

#推荐用get()如果键名不存在，不报错返回None 还可以传入默认值get(key,defalut-value)
