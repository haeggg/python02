# 개별 실습 8-1

names = ["전해인", "김민정", "정이름", "홍길동", "김그린"]

# 처음 세 명
print(names[:3])

# 마지막 두 명
print(names[-2:])

# 역순(오른쪽에서 왼쪽으로) 명단 / 1이면 왼쪽에서 오른쪽으로
print(names[::-1])


#개별 실습 8-2

scores = [70, 85, 90, 60, 95]
print(scores[1:4], scores[::2])

scores.append(88)
scores.sort()
#sort() : 원본 리스트 자체를 정렬

print(scores)
print(scores[0], scores[-1], len(scores))
# len() : 데이터의 길이(개수)를 알려주는 내장 함수

point = (3, 4)
x, y = point
print (x * y)