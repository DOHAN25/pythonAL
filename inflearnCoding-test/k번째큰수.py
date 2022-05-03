import random as r

num1, num2 = map(int, input("N과 K입력: ").split())

a = list(map(int, input("베열: ").split()))

res = set() # set 자료구조는 중복을 제거한다.

for i in range(num1):
    for j in range(i + 1, num1):
        for k in range(j + 1, num1):
            res.add(a[i] + a[j] + a[k]) # 중복을 제거하면서 담기

res = list(res)

res.sort(reverse=True)
print(res[num2-1])



