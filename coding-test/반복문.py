# 특정한 소스코드를 반복적으로 실행하고자 할때 사용한다.

# while
i = 1
result = 0
while i <= 9:
    result += i
    i += 1

print(result)

# 반복문을 작성할때는 무한루프를 항상 생각하고 반복문을 탈출할 수 있는지 확인해야 한다.

# for
# for 변수 in 리스트:
#      실행할 소스코드
array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용한다.
# 이때 range(시작 값, 끝 값 + 1) 형태로 사용한다.
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 된다.
result = 0

for i in range(1, 10):
    result += i

print(result)

# 파이썬의 continue 키워드
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할ㄷ 때 continue 를 사용한다.
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i
print(result)

# 파이썬의 break 구문
# 반복문을 즉시 탈출하고자 할 때 사용한다.
i = 1
while True:
    print("현재 i의 값 :", i)
    if i == 5:
        break
    i += 1
