# 실습 8

items = ["book", "pen", "bag"]

print(items[0], items[-1])  # 인덱스 위치에 값 가져옴
print(items[1:3])   # 슬라이스 start:stop:step 범위 선택

items.append("cup") # 마지막 인덱스 추가
items[0] = "note"   # 0 인덱스 수정

print(items)

point = (10, 20)
x, y = point
print(x, y)