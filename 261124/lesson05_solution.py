# 실습 5-2
# 1~10 중 짝수만 더하기

total = 0

for number in range(1, 11):
    if number % 2 != 0:
        continue
    total += number

print(total)

# for문 범위를 지정해 줄 때는 in 뒤에 range(start 값, end 값) 설정