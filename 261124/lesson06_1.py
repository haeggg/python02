# 개별 실습 6
# 넓이 함수와 결과 확인

# 함수 정의
def area(width, height):
    c = width * height
    return c

# 입력 후 처리
a = input("가로: ").strip()
b = input("세로: ").strip()

aa = int(a)   #int로 변경
bb = int(b)   #int로 변경

result = area(aa, bb)

print(f"넓이는 {result} 입니다.")