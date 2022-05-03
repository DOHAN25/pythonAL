

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')

print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2 == 1:
        print(x, end=' ')

# 인덱스 값에 가고 싶을 때 -> 튜플자료형으로 조회
for x in enumerate(a):
    print(x)

# 튜플
b = (1, 2, 3, 4, 5)
print(b)
print(b[0])
# 튜플과 리스트의 차이점은 튜플은 값 변경이 안된다. 절대 절대 절대 = 핟당(assignment)

for x in enumerate(a):
    print(x[0], x[1])
print()
print()

for index, value in enumerate(a):
    print(index, value)

print()
print()

# all 모두 참 일때
if all(50>x for x in a):
    print("Yes")
else:
    print("No")


# 한개라도 참인것이 있으면 true -> any false 는 모두가 거짓일 때
if any(15 > x for x in a):
    print("Yes")
else:
    print("No")


