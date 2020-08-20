# -*- coding:utf-8 -*-

# 1부터 45 사이의 숫자 6개를 
# 중복 없이 만들어서 
# 리스트로 리턴하는 lotto() 함수 만들자
# main함수에서 호출하여 출력하자.
import random


def ran01():
    list = []
    ran_num = random.randint(1, 45)
    
    for i in range(0,6):
        while ran_num in list:
            ran_num = random.randint(1, 45)
            
        list.append(ran_num)
    list.sort()
    return list

if __name__ == '__main__':
    print(ran01())
    