# -*- coding:utf-8 -*-

from pymongo import MongoClient

# MongoDB랑 연결
# client = MongoClient('127.0.0.1', 27017)
client = MongoClient('mongodb://localhost:27017')

# 연결된 client에서 db와 연결
# db = client.test
db = client['test']
    
# 연결된 db에서 collection 가져오기
# collection = db.score
collection = db['score']


for doc in collection.find():
    print(doc)