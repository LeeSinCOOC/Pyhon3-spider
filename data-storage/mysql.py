import pymysql

db = pymysql.connect(
        host='localhost',
        user='root',
        password='chen0824',
        port=3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print(data)
cursor.execute('create database spiders default character set utf8')
db.close()

#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()

#原子性
#一致性
#隔离性
#持久性

######
'''
fetchone()
fetchall() --- 当前指针到结束的所有数据，而不是直接取所有的数据，如果前面取了一个，指针会停在当前位置