# 실습 1
# VS Code와 첫 파이썬 프로그램

import sys

print("hello python")
print("수업 시간: ", 60)
print("실행기: ", sys.executable)

# 실행기 
# import sys 후 sys.executable로 사용

# 추가
print("python", "vs code", "터미널", sep=" | ")
print("버전: ", sys.version.split()[0])
print("한 줄로", end=" ")
print("이어서 출력")