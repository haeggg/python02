# 실습 7
# 가변 인자와 람다 함수

def sum_values(*args):
    return sum(args)

def profile(**kwargs):
    return kwargs

print(sum_values(3,5,7))
print (profile(name = "민수", level = "basic"))

items = [("pen", 1500), ("book", 12000)]
print(sorted(items, key=lambda item: item[1], reverse=True)) # reverse=True 내림차순 정렬

print(sorted(items, key=lambda item: item[:1]))
# sorted() : 리스트나 여러 요소를 정렬해 주는 함수 / 데이터를 오름차순이나 내림차순으로 정리해 주는 역할

# *args : 추가 위치 인수를 튜플로 수집
# ** kwargs: 추가 키워드 인수를 딕셔너리로 수집

# lambda : 한 표현식의 결과를 반환하는 익명 함수
# key : 정렬 때 비교할 값을 만드는 함수

# key = lambda ~ : ~

# item > 현재 검사하고 있는 요소 (미리 정해져 있는 특별한 단어가 아니라 개발자 마음대로 바꿔도 됨)
# item[1] > 그 요소의 두 번째 값