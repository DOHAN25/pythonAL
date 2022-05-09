

people_num=int(input("게임에 참여하는 사람의 수를 입력해 주세요: "))

res=0
reward_list=[]
for i in range(people_num):
    tmp=input("주사위 숫자:").split()
    tmp.sort()
    num1, num2, num3 = map(int, tmp)
    if num1==num2 and num2==num3:
        reward=10000+num1*1000
    elif num1==num2 or num1==num3:
        reward=1000+(num1*100)
    elif num2==num3:
        reward=1000+(num2*100)
    else:
        reward=num3*100
    if reward>res:
        res=money

print(res)



