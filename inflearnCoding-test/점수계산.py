num = int(input("문제의 개수를 입력해 주세요: "))


input = list(map(int, input("채점 결과를 입력해 주세요: ").split()))

sum=0
cnt=0

for x in input:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(sum)





