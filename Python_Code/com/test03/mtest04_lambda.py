# -*- coding:utf-8 -*-

# lambda function : 익명함수 -> 함수를 만들지 않고,
#                   선언만 해두고(파이썬에서는 없음), 필요할 때 바디를 
#                   만들어서 사용(자바에서의 람다)

# def func01(a, b)
    # return a + b
    
# 에로우 펑션!
hap01 = lambda a, b: a + b
print(hap01(10, 20))

gob = lambda a, b : a * b
print(gob(30, 40))

hap02 = lambda a, b, c : a + b + c
print(hap02(3, 4, 5))

# 리스트안에 튜플 4개가 들어가있음
a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
print(a)
a.sort(key=lambda a: a[1])  # 처음 a에 들어가는게 () 튜플 하나하나가 들어갈거임
# a[1]의 뜻은 'one', 'two', 'three', 'four' 기준으로 정렬 해주세요.
# 그래서 f 다음 o 그다음 th 그다음 two가 나온것임
print(a)


min01 = (lambda x, y : x if x < y else y)
# x, y 입력 받아서 if문이 참이면 x를 거짓이면 y를 리턴
# 뒤에서부터 읽어들임 
print(min01(11, 22))

max01 = (lambda x, y : x if x > y else y)
print(max01(10, 23))

b = lambda x: (lambda y: x + y)
c = b(100) # lambda y : 100 + y
d = c(90)  # 100 + 90
print(d)
print(b(100)(90)) # c 랑 d가 합쳐져있음 결국 190 같은 뜻

# 1 ~ 100 사이의 숫자 중 5의 배수를 출력하자
e = lambda x: bool(x % 5) # x의 값이 5의 배수가 들어오면 bool(0)이 됨 (false가 됨) 
# 0은 false뜻임 true는 0이외의 숫자들 1,2,3,4 등등등
five = [i for i in range(1, 101) if not e(i)]
# i가 e에 들어가서 false가 나오면(5의 배수라면) 다시 그걸 true로 바꿔서 i를 리스트안에 넣는다.
# five = []
# for i in range(1, 101):
    # if not e(i):
        # five.append(i) 이거와 같은 뜻
print(five)


# None == null
f = lambda x: x if (x % 5 != 0) else None
result = [i for i in range(1, 101) if not f(i)]
print(result)

# 리스트를 만들거야 그리고 i를 리턴할거야 이 다음 반복문 돌기
result_five = [i for i in range(1, 101) if not (lambda x: x if(x % 5 != 0) else None)(i)] 
print(result_five)
# 5의 배수면 None을 리턴해서 그걸 not으로 바꾸고
# 5의 배수가 아니면 그걸 리턴해서 not으로해서 None으로 바꿈