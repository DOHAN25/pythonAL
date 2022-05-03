

'''
a = [0]*3
print(a)
'''


# 2차원 배열 생성
a = [[0]*3 for _ in range(3)]
print(a)
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

print()

for x in a:
    print(x)

print()

for x in a:
    for y in x:
        print(y, end=' ')
    print()