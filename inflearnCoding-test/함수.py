
'''
def add(a, b):
    c = a + b
    print(c)

add(10, 15)
'''

# 함수는 메인 스크립트보다 위에 해야한다. 그니까 무조건 함수 선언이 함수 실행보다 먼저 와야 한다.


def add(a, b):
    c = a + b
    return c
'''
print(add(3, 4))
'''

# 튜플 자료구조로 리턴된다.
def add(a, b):
    c = a + b
    d = a - b
    return c, d

# print(add(3, 4))

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]

for x in a:
    if isPrime(x):
        print(x, end=' ')










