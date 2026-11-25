# 실습 7
# 가변 인자와 람다 함수

def sum_values(*args):
    return sum(args)

def profile(**kwargs):
    return kwargs

print(sum_values(3,5,7))
print (profile(name = "민수", level = "basic"))

items = [("pen", 1500), ("book", 12000)]
print(sorted(items, key=lambda item: item[1], reverse=True))

print(sorted(items, key=lambda item: item[:1]))

# *args : 추가 위치 인수를 튜플로 수집
# ** kwargs: 추가 키워드 인수를 딕셔너리로 수집

# lambda : 한 표현식의 결과를 반환하는 익명 함수
# key : 정렬 때 비교할 값을 만드는 함수

# key = lambda ~ : ~