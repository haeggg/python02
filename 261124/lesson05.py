# 실습 5-1
# for / while 반복문과 흐름 제어

total = 0 

for quantity in [1, 0, 3]:
    if quantity == 0:
        continue
    total += quantity

print(total)

attempts = 0
while attempts < 3:
    attempts += 1
    if attempts == 2:
        break

print(attempts)

# break 가장 안쪽 반복문을 종료
# continue 현재 회차의 나머지를 건너뜀

# for (변수) in (조건) > 변수가 조건일 때까지 반복
# while은 변수 초기화 후 while (조건)