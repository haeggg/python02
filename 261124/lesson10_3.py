def clean_quantities(raw_values):
    valid, errors = [], []

    for raw in raw_values:
        try:
            value = int(raw)

            if not 1 <= value <= 100:
                raise ValueError("range")
                # raise 코드에서 예외(에러)를 강제로 발생시키는 키워드
            
            valid.append(value)

        except ValueError:
            errors.append(raw)

    return valid, errors


values, errors = clean_quantities(["2", "bad", "0", "3"])

totals = [quantity * 8000 for quantity in values]
report = {str(i + 1): value for i, value in enumerate(totals)}

# enumerate 리스트, 튜플, 문자열 같은 순회 가능한 객체를 반복할 때
# 인덱스(순서)와 값을 (인덱스, 값) 튜플 형태로 함께 반환하는 파이썬 내장 함수

print(values, errors)
print(report, sum(totals))