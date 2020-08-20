# -*- coding:utf-8 -*-

def func01(x, y):
    return x + y
    
def func02(x, y):
    return (x + y), (x - y)
    # return (x+y, x-y)
    
    
if __name__ == '__main__':
    a = func01(1, 3)
    print(a)
    b, c = func02(4, 7)
    # b = func02(4,7)
    print(b, c)
    # print(b) 패킹!! 튜플에 넣어줌
    # c, d = func02(5, 3)
    # print(c, d) 언패킹!