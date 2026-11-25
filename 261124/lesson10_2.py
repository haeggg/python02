# 개별 실습 10-2

raw = ["3", "x", "7", "", "12"]
numbers = []

for value in raw:
    try:
        numbers.append(int(value))
    except ValueError:
        print("건너뜀: ", repr(value))
        # 객체를 개발자용 공식 문자열로 변환하는 내장 함수
        # ex : (문자열임을 알 수 있도록 따옴표가 붙음)

squares = [n * n for n in numbers if n % 2 == 1]
labels = {n : "짝수" if n % 2 == 0 else "홀수" for n in numbers}

print(numbers, squares)
print(labels)