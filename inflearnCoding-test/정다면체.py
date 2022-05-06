
n, m = map(int, input("N과 M입력: ").split())

result = [0]*(n+m+3)
max=0
for i in range(1, n+1):
    for j in range(1, m+1):
        result[i+j] += 1

for i in range(n+m+1):
    if result[i]>max:
        max=result[i]

for i in range(n+m+1):
    if result[i]==max:
        print(i, end=' ')











