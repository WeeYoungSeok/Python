# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test']
score = db['score']

# name이 자기이름인 document 하나를 찾아서, 국어점수를 0점으로 만들자
result01 = score.update_one({'name': '위영석'}, {'$set':{'kor': 0}})
# 하나만 바꾸기!
print(result01.matched_count)
print(result01.modified_count)

print('-----')

# 여러개 바꾸기
result02 = score.update_many({'eng': 70}, {'$set':{'eng':0}})
# 찾은 갯수
print(result01.matched_count)
# 수정된 갯수
print(result01.modified_count)