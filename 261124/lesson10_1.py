# 개별 실습 10
# 점수 문자열 목록에서 0~100의 정수만 남기고
# 60점 이상인 점수 목록과 오류 입력 목록을 출력하세요.

raw_score = ["50", "80", "90", "abc", "-1", "101"]
scores, errors = [], []

for raw in raw_score:
    try:
        score = int(raw)
        
        if not 0 <= score <= 100:
            raise ValueError("range")
        
        scores.append(score)
    
    except ValueError:
        errors.append(raw)

passed = [score for score in scores if score >= 60]
print("패스한 점수: ", passed)
print("오류 목록: ", errors)
