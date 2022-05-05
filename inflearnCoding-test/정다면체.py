
n, m = map(int, input("N과 M입력: ").split())

result = list(range(2, n+m+2))

print(result)

for i in range(1, n+1):
    for j in range(1,  m+1):
        print(i, j)



result.sort()

print(result[range(result)])





