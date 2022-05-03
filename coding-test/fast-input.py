import sys

# 문자열 빠르게 입력받기
data = sys.stdin.readline().rstrip()
print(data)

# 파이썬에서 기본 출력은 print() 함수를 사용한다.
# 기본적으로 출력 이후에 줄 바꿈을 수행한다.
# 줄 바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있다.

print(1, 2)
print(6, end=" ")

# f-string
# 파이썬 3.6부터 사용 가능하며, 문자열 앞에 접두사 'f'를 붙여 사용한다.
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.
answer = 7
print(f"정답은 {answer} 입니다.")