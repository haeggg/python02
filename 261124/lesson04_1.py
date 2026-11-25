# 개별 실습 4
# 점수 범위 검사와 학점 판정

score = input("점수: ").strip()
score_1 = int(score)

if score_1 < 0 or score_1 > 100:
    grade = "점수 입력 오류"
elif score_1 >= 90:
    grade = "A"
elif score_1 >= 80:
    grade = "B"
else:
    grade = "C"

print("결과: ", grade)