# 실습 10
# 컴프리헨션과 예외 처리 종합 실습

#enumerate

values = [2, 3, 0]
totals = [n * 8000 for n in values if n > 0]
report = {str(i + 1) : v for i, v in enumerate(totals)}

print(totals)
print(report)

# except

try:
    quantity = int("abc")
except ValueError:
    print("정수를 입력하세요")
