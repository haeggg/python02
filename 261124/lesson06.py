# 실습 6
# 함수 정의와 매개변수, 반환값

def quote(price, quantity, shipping = 3000):    # 매개변수 기본값 설정 가능
    subtotal = price * quantity
    return subtotal + shipping


total = quote(8000, 3)
print(total)

print(quote(8000, 3, shipping=0))   # 매개변수 기본값 변경 가능

# def : 함수 정의를 시작하는 키워드