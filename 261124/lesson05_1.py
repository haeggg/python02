# 개별 실습 5

# 1. 짝수 더하기

total = 0

for number in range(1, 11):
    if number % 2 != 0:
        continue
    total += number

print("짝수 합계: ", total)
print("=================")


# 2. 홀수 더하기

total = 0

for number in range(1, 11):
    if number % 2 == 0:
        continue
    total += number

print("홀수 합계: ", total)
print("=================")


# 3. 짝수 값들이 출력

print("짝수값")

for number in range(1, 11):
    if number % 2 != 0:
        continue
    print(number)

print("=================")

# 4. 홀수 값들이 출력

print("홀수값")

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)