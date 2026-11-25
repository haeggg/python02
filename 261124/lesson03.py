# 실습 3
# 문자열과 입력값 변환


name = input("이름: ").strip()
raw_quantity = input("수량: ")
quantity = int(raw_quantity)    # str 값을 정수로 변환
total = quantity * 8000

print(f"{name}님, 총액: {total:,}원")
print("book,pen".split(","))

# input : 터미널에서 한 줄의 입력을 받는 함수 > java에 scanner와 동일한 역할을 함
# strip : 문자열 양끝 공백을 제거하는 메서드
# f-string(f"~") : 변수 값을 문장 안에 넣는 문자열 표기
# split : 문자열을 특정 기준으로 나누어 리스트(list)로 만들어 주는 함수 (괄호 안에는 구분 기호 표시)
