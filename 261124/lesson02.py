# 실습 2
# 변수의 기본 자료형, 연산자

import sys

price = 12000           #int 형
quantity = 3            #int 형
discount_rate = 0.1     #float 형
product = "노트"         #str 형
is_member = True        #bool 형

subtotal = price * quantity

print(product, subtotal)
print(type(price).__name__, type(discount_rate).__name__)
print(subtotal >= 30000, is_member)
print(7 / 2 , 7 // 2, 7 % 2)

# type(-) 변수에 저장된 값의 자료형을 확인하는 파이썬 내장 함수
# .__name__ 은 자료형 객체에서 이름만 꺼내오는 속성(attribute)

# / 일반 나눗셈 | // 몫만 구하는 나눗셈 | % 나머지만 구하는 나눗셈