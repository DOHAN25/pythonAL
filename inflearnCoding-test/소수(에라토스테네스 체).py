
num = int(input("숫자를 입력해 주세요. : "))

make_list=[0]*(num+1)
count=0

for i in range(2, num+1):
    if make_list[i]==0:
        count+=1
        for j in range(i, num+1, i):
            make_list[j]=1

print(count)




