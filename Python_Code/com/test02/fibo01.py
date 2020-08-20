# -*- coding:utf-8 -*-

# fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 ...
# a b
#   a b
#     a b
# ...


# 5를 넣으면 0부터 4까지 반복
n = input('input n : ')
a, b = 0, 1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a + b
    # a자리에 b값 넣고 
    # b자리에 a랑 b랑 더한값을 넣는다.
    i += 1