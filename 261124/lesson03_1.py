# 개별 실습 3-1
# 입력 값을 정리하고 정수로 바꾸기

product = input("상품명: ").strip()
quantity = input("수량: ")

quantity_1 = int(quantity)

print(f"상품: {product} / 수량: {quantity_1}")


# 개별 실습 3-2
# 문자열 정리 · 분리 · 결합과 숫자 변환

raw = " book,pen,bag "
items = raw.strip().split(",")
print(items)
print(" / ".join(items).upper())

price = int("12000")
print(f"단가 {price:,}원, 상품 {len(items)}개")
print("pen" in items, raw.count("b"))