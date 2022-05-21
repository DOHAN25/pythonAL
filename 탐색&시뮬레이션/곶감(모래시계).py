# 현수는 곶감을 ㅁ나들기 위해 감을 깎아 마당에 말리고 있습니다.
'''
현수의 마당은 N*N 격자판으로 이루어져 있고, 현수는 각 격자단위로 말리는 감의 수를 정한다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않는다. 그래서 현수는 격자의 행을 기준으로
왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 한다.
'''



n=int(input("n:"))
list1=[list(map(int, input(":").split())) for _ in range(n)]

m=int(input("m:"))

for i in range(m):
    a, b, c=map(int, input("a, b, c:").split())
    if b==0:
        for _ in range(c):
            list1[a-1].append(list1[a-1].pop(0))
    else:
        for _ in range(c):
            list1[a-1].insert(0, list1[a-1].pop())

for x in list1:
    print(x)

sum=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        sum+=list1[i][j]
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1


print(sum)


