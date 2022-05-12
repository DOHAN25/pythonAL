'''
n개의 수로 된 수열이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합이 m이되는 경우의 수를 구하여라.
'''



n,m=map(int,input().split)
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)

