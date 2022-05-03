# 함수란 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미한다.
# 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있습니다.

# 함수의 종류
# 1. 내장함수 : 파이썬이 기본적으로 제공하는 함수
# 2. 사용자 정의 함수 : 개발자가 직접 정의해서 사용할 수 있는 함

# global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()
print(a)


# 람다 표현식
# 간단하게 작성할 수 있다.
print((lambda a, b: a + b)(3, 7))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)

print(list(result))