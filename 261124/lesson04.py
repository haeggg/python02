# 실습 4
# 조건문과 논리 연산

total = 30000
is_member = False

if total < 0:
    message = "금액 오류"
elif total >= 30000 or is_member:
    message = "무료 배송"
else:
    message = "배송비 3000원"

# (자바) 괄호는 (파이썬) 콜론 : 로 (자바) 중문은 (파이썬) 들여쓰기로

print(message)
