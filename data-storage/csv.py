import csv

with open('data.csv','w') as f:
    writer = csv.writer(f,delimiter=' ') #delimiter 改分隔符 不改为,
    writer.writerow(['id','name','age'])
    writer.writerow(['1','mik','11'])
    writer.writerow(['2','bob','13'])
    writer.writerow(['3','jodan','15'])
    
# writerows 写入多行，嵌套列表就可以了
    
#结构化数据，也可以用字典写入
with open('data.csv','a') as f:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writerow({'id':'33','name':'yy','age':'66'})
