"""
功能：python中MongoDB基本使用方法关于
	连接MongoDB、指定数据库、指定集合、插入数据、查询数据、计数、排序、偏移、更新、删除这10个功能代码块的实现方法
日期：2019/3/27
editor：Shrimay1
"""
import pymongo
from bson.objectid import ObjectId
#连接MogoDB
client = pymongo.MongoClient(host='localhost',port=27017)
#指定数据库
db = client.test
#指定集合
collection = db.students

student1 = {
	'id':'20170101',
	'name':'ShirMay1',
	'age':23,
	'gender':'felmale'
	}
student2 = {
	'id':'20170102',
	'name':'Hardon',
	'age':20,
	'gender':'male'
	}
student3 = {
	'id':'20170103',
	'name':'Jordan',
	'age':20,
	'gender':'male'
	}
student4 = {
	'id':'20170104',
	'name':'Mike',
	'age':21,
	'gender':'male'
	}
student5 = {
	'id':'20170105',
	'name':'Kevin',
	'age':20,
	'gender':'male'
	}
#insert_one()插入单条数据
insert_result = collection.insert_one(student1)
print(insert_result)
print(insert_result.inserted_id)

#insert_many()插入多条数据
insert_result = collection.insert_many([student2,student3,student4,student5])
print(insert_result)
print(insert_result.inserted_ids)

#find_one()方法查询name为Mike的数据
query_result = collection.find_one({'name':'Mike'})
print(type(query_result))
print(query_result)

#find_one()方法根据ObjectId来查询
query_result_id = collection.find_one({'_id': ObjectId('5c9b36b5fe0bea232819c8ea')})
print(query_result_id)

#find()方法查询年龄为20的数据
query_result_ages = collection.find({'age':20})
print(query_result_ages)
for result in query_result_ages:
    print(result)
    
#find()方法查询年龄大于20的数据
query_ages20 = collection.find({'age':{'$gt':20}})
print(query_ages20)
for result in query_ages20:
    print(result)


#count_documents()方法计数
count = collection.count_documents({})
print(count)
count1 = collection.count_documents({'age':20})
print(count1)

#sort()方法排序
sort_result = collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in sort_result])

#偏移
skip_result = collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in skip_result])

#偏移取1个结果
skip_result1 = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(1)
print([result['name'] for result in skip_result1])

#update_one()更新name为Kevin的数据的年龄
condition = {'name':'Kevin'}
student = collection.find_one(condition)
student['age'] = 24
result = collection.update_one(condition,{'$set':student})
print(result)
print(result.matched_count,result.modified_count)

#update_one()更新年龄大于20的年龄加1
condition = {'age':{'$gt':20}}
result = collection.update_one(condition,{'$inc':{'age':1}})
print(result)
print(result.matched_count,result.modified_count)

#update_many()更新年龄大于20的年龄加1
condition = {'age':{'$gt':20}}
result = collection.update_many(condition,{'$inc':{'age':1}})
print(result)
print(result.matched_count,result.modified_count)

#删除
result = collection.delete_one({'name':'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age':{'$lt':25}})
print(result.deleted_count)
