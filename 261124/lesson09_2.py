# 개별 실습 9-2
# 딕셔너리 수정 · 순회와 JSON 저장 · 복원

import json

stock = {"book" : 3, "pen" : 10}

stock["bag"] = 2
stock["pen"] -= 4

print(stock.get("cup", 0), stock["pen"])

for name, count in stock.items():
    print(name, count) #name 에는 딕셔너리 key 값 / count 에는 딕셔너리 값 입력 후 출력
# items() : 파이썬 딕셔너리에서 키(Key)와 값(Value)을 한 쌍씩 가져오는 메서드

text = json.dumps(stock, ensure_ascii=False)
loaded = json.loads(text)

print(text, loaded == stock)
print(sorted({"a", "b", "c"} - {"b"}))