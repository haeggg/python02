# 실습 9 
# 딕셔너리 / JSON / 집합

import json
# json : 객체 · 배열 등을 표현하는 텍스트 규격

student = {"name" : "민수", "score" : 80}
# dict(딕셔너리) : 키에 값을 대응시키는 자료구조

student["score"] += 5

print(student.get("city", "미입력"))
# = student.get("찾을 키", "키가 없을 때 대신 반환할 값")

text = json.dumps(student, ensure_ascii=False)
# 파이썬 객체 → JSON 문자열

# dumps() : 파이썬 객체를 JSON 문자열로 변환하는 함수
# ensure_ascii=False : 한글 같은 비ASCII 문자를 어떻게 표현할지 결정하는 옵션

print(json.loads(text)["score"])
# JSON 문자열 → 파이썬 객체

#loads() : JSON 문자열을 파이썬 객체로 변환하는 함수


a = {"book", "pen", "book"}
b = {"pen", "bag"}
# set(셋) : 중복 없는 항목의 모음

print(sorted(a & b))
print(sorted(a - b))