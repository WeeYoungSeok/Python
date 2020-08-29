# -*- coding:utf-8 -*-


def factorial(n):
    sum = 1
    for i in range(n,0,-1):
        sum *= i
    return sum

# 재귀함수
def factorialRecursion(n):
    # 종료 조건!!!
    if n == 1:
        return 1
    else:
        return n * factorialRecursion(n-1)
    


if __name__ == '__main__':
    n = int(input('input n : '))
    print('{} factorial = {}'.format(n, factorial(n)))
    print('{} factorial = {}'.format(n, factorialRecursion(n)))