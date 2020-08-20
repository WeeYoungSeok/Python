# -*- coding:utf-8 -*-

i = 1

while i <= 10:
    print(i)
    i += 1
    # python 에는 ++가 없다!!

print()
# while을 사용하여 1 ~ 10까지의 총 합계 출력

j = 1
mysum = 0

while j <= 10:
    mysum = mysum + j   # mysum += j
    j += 1
else:
    print('합계 :' ,mysum)
    # j는 11이 된 상태에서 종료됨