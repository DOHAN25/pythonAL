


import random as r

a = []
print(a)
b = list()
print(b)

a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

b = list(range(1, 10))
print(b)


c = a + b
print(c)



print()
print()

a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)
a.pop(3)
print(a)

#remove는 값을 찾아서 지워준다.
a.remove(4)
print(a)

print(a.index(5)) # 5라는 값의 인덱스를 알려준다.


a = list(range(1, 11))
print(a)
print(sum(a)) # a라는 리스트의 값을 모두 더해준다.
print(max(a)) # 리스트의 최고값을 찾아준다.
print(min(a))

# sum/ min / max 함수는 인자로 값는 것의 대해서 구해준다.
# ex) min(7,3)은 7과 3비교해서 3이 나온다.


# random함수의 shuffle 함수
r.shuffle(a)
print(a)
a.sort() # 오름차순 정렬
print(a)
a.sort(reverse=True) # 내림차순 정렬
print(a)
a.clear() # 초기화
print(a)