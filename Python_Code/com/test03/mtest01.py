# -*- coding:utf-8 -*-

# python 함수 : def
def func01():
    print('함수 1 입니다.')
    
def func02():
    return '함수 2 입니다.'
    
def func03():
    return {1: 'a', 2: 'b'}
    
if __name__ == '__main__':
    # 프로그램의 주 진입점
    print('프로그램 시작 시 가장 먼저 호출됨...')
    func01()
    print(func02())
    print(func03()[1])  # [키값]넣으면 value 나옴