# -*- coding:utf-8 -*-

# 여기에 import해도 상관없음

# split
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')    # 공백 기준으로 자르기
print(arr01)                # 결과값이 list의 형태이다!

arr02 = str01.split(' ', 1) # 공백 기준으로 자를건데 공백 하나만 잘라주세요
print(arr02)                # 이때 하나의 뜻은 공백의 갯수를 의미


# 파이썬에서는 import를 필요한 부분에서 선언함
# 약속은 아니다. 자바 개발자는 맨 위에 선언하는걸 좋아함
import re
arr03 = re.split('[\s]|[,]', str01)
print(arr03)
print()

# join
arr04 = ['1', '2', '3', '4']
print(arr04)
a = '+'.join(arr04)
print(a)

# eval은 문자열 연산기호를 실행해줌
# 외부에서 Path입력시 실행이 되어버려서 보안적으로 굉장히 취약함
# 되도록이면 쓰지말자.
print(eval(a))

