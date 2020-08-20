# -*- coding:utf-8 -*-

i = 1

while i <= 10:
    if i > 5:
        break
    print(i, end=' ')
    i += 1
else:
    print('i',i,sep='=')    # while문이 10까지 정상적으로 반복하지 않고 끝났기 때문에 출력 x
    
print()

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i ,end=' ')
else:
    print('i',i,sep='=')
    
##########
# while의 실행 결과 : 1 2 3 4 5 (한줄씩)
# for의 실행 결과 :  1 3 5 7 9 i=10 (한줄씩)