# 개별 실습 9
# 두 반의 수강과목을 집합으로 비교하고, 학생 정보를 json으로 저장할 수 있는 문자열로 만드세요.

import json

class_a = {"국어", "영어", "수학", "미술"}
class_b = {"수학", "영어", "한국사", "사회"}

print("a반: ", class_a)
print("b반: ", class_b)

# 공통 과목 계산 
print("")
print(f"공통 과목: {sorted(class_a & class_b)}")

# 한 반에만 있는 과목 계산
print(f"a반에만 있는 과목: {sorted(class_a - class_b)}")

# 모든 과목 계산
print("")
print(f"전체 과목: {sorted(class_a | class_b)}")

# dict에 name과 subject 저장
# dump 전에 set{}을 정렬된 list[]로 변환

student = {"name" : "해인", "subject" : sorted(class_a | class_b)}
text = json.dumps(student, ensure_ascii=False)

print("")
print(text)

print("")
print(json.loads(text)["name"])
print(json.loads(text)["subject"])