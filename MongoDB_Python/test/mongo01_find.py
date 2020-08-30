# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

# 도큐먼트들을 전부 묶어서 그 전체의 객체를 cursor에 담은거임
# 0번지 1번지 ... 이걸 cursor가 반복문들 통해 하나씩 빼오는거임
# 그러면 0번지에대한 애들나옴
# 그걸 밑에서 for in문을 통해 가져올거
cursor = score.find()
print(cursor)

for doc in cursor:
    # pprint는 mongodb에서의 pretty를 의미
    pprint.pprint(doc)
    
print('-----')

# 하나만 가져와서 cursor 객체로 가져와짐(객체 덩어리)
lee = score.find({'name': '이순신'})
print(lee)

# 하나만 가져오더라도 반복문을 통해 뽑아야함
for doc in lee:
    print(doc)
    
print('-----')

hong = score.find_one({'name': '홍길동'})
pprint.pprint(hong)

print('-----')

cursor = score.find({'kor':{'$gt': 60 }})
for doc in cursor:
    pprint.pprint(doc)
    
print('-----')

print('score collection 안에 있는 document의 총 갯수 : ', score.count_documents({}))