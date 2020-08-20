# -*- coding:utf-8 -*-

# 1. for문을 사용하여 구구단을 전체 출력하는 함수 gugu()를 작성하고, main함수에서 호출
# 2. while문을 사용하여 구구단 중 파라미터 전달된 단만 출력하는 함수 gugudan(x)를 작성하고, main함수에서
#    콘솔을 통해 n을 입력받아 호출하자.


def gugu():
    for i in range(2, 10):
        print(str(i) + '단')
        # print('<<%d단>>' % i)
        for j in range(1, 10):
            print('{} * {} = {}'.format(i,j,i*j))
            # print('%d * %d = %d' %(i, j, i*j))
        print()
    # pass 입력하면 이 함수는 패스 실행안함
        
def gugudan(x):
    i = 1
    print(x + '단')
    while i <= 9:
        print('{} * {} = {}'.format(x,i,int(x)*i))
        # 문자열 입력 받아서 int로 형변환
        i += 1
    else:
        print('구구단 끝!')
            
            
if __name__ == '__main__':
    gugu()
    
    n = input('구구단 n단 입력 : ')
    print()
    gugudan(n)