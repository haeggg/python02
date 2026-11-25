# 개별 실습7

# 여러 가격을 받아 합계를 반환 / 상품 목록을 이름 길이가 짧은 순으로 정렬

def basket_total(*prices):
    return sum(prices)

print("가격 합계: ", basket_total(1500, 12000, 800, 2000, 20000))

items1 = ["펜", "다이어리", "지우개", "공책", "물감"]

print(sorted(items1, key=lambda name: len(name)))



# 5개의 제품명과 가격을 받은 후 받은 가격을 내림차순으로 정렬

items2 = [("펜", 1500), ("다이어리", 12000), ("지우개", 800), ("공책", 2000), ("물감", 20000)]

print(sorted(items2, key=lambda item: item[1], reverse=False)) #정렬 reverse

