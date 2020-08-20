# -*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']

# 해당 반복문이 정상적으로 종료되었을때 else 실행 (python 한정)
for i in subject:
    # 출력하고 공백 붙여주자
    print(i, end=' ')
else:
    print('재밌다')
    
for i in range(1, 100):
    # 출력하고 + 붙여주자
    print(i, end='+')
    
print('\n구구단')
for i in range(2, 10):
    print('<<'+str(i)+'단>>')
    for j in range(1, 10):
        # print(str(i) + ' * ' + str(j) + ' = ' + str(i * j))
        # print(str(i), '*', str(j), '=', str(i * j), sep='   ')
        print('{} * {} = {}'.format(i,j,i*j))
        
for i in range(10, 0, -1):
    print(i, end=' ')
    # 10부터 0까지 -1씩 증가
    # range 세번째 숫자를 생략하면 +1씩
