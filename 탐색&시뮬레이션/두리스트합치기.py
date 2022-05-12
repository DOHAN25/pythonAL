# 오름차순으로 정렬된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐서 출력하는
# 프로그램을 작성하여라


'''
첫 번째 줄에 첫 번째 리스트의 크기 N이 주어진다.
두 번째 줄에 n개의 리시트 원소가 오름차순으로 주어진다.
세 번째 줄에 두 번째 리스트이 크기 m이 주어진다.
네 번째 줄에 m개의 리스트 원소가 오름차순으로 주어진다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않는다.
'''

'''
n = int(input("n:"))
list1=[]
list2=[]
for i in range(n):
    a = int(input("리스트:"))
    list1.append(a)

m = int(input("m:"))

for i in range(m):
    b = int(input("리스트:"))
    list2.append(b)

result= list1+list2

result.sort()
print(result)
'''

# 위의 풀이는 너무 오래걸린다.
# sort 함수는 8개의 원소가 있으므로 8logn 이 소요된다.
# 포인터를 생각하는게 포인트
n=int(input("n:"))
a=list(map(int, input("리스트1:").split()))
m=int(input("m:"))
b=list(map(int, input("리스트2:").split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

print(c)