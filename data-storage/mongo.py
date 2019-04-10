import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)

db = client.test # db = client['test']

collection = db.students

#插入数据
student = {
        'id':'123',
        'name':'bob',
        'age':20}
result = collection.insert(student) #不推荐insert 建议insert_one/many()
print(result) 

query = collection.find_one({'name':'bob'})
print(type(query))
print(query)

results = collection.find({'age':20})
for i in results:
    print(i)
    
# result = collection.find({'age':{'$gt':20}}) 还可以正则匹配

results = collection.find({'age':20}).count() #计数
results = collection.find({'age':20}).sort('name',
                         pymongo.ASCENDING/pymongo.DESCENDING)#排序
results = collection.find({'age':20}).skip(2) #偏移
results = collection.find({'age':20}).limit(2) #指定个数

#更新
condition = {'name':'kk'}
student = collection.find_one(condition)
student['age'] = 24
result = collection.update(condition,student)

result = collection.update(condition,{'$set':student})
    
    
    
    