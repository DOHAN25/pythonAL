# 내장함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공한다.

# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공한다.
              # 특히 순열과 조합 라이브러리에는 자주 사용된다.

# heapq : 힙 자료구조를 제공한다.

# bisect : 이진 탐색(Binary Search) 기능을 제공한다.

# collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함한다.

# math : 필수적인 수학적 기능을 제공한다.

# 자주 사용되는 내장 함수
# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval() 수 형태로 바꿔준다.
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동, 35'), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)


# 순열과 조합
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것

# 순열
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# 조합
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)

# 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다.
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(dict(counter)) # 사전 자료형으로 반환

# 최대 공약수와 최소 공배수
import math
# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14
print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14)) # 최소 공배수(LCM) 계산
