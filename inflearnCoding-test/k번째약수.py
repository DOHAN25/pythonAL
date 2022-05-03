
a, b = map(int, input("숫자를 입력해 주세요: ").split())
count = 0
result = 0
for i in range(1, a+1):
    if a%i == 0:
        count += 1
    if count == b:
        print(i)
        break
else:
    print(-1)
