

people_num=int(input("게임에 참여하는 사람의 수를 입력해 주세요: "))

reward=0
reward_list=[]
for i in range(people_num):
    tmp=input("주사위 숫자:").split()
    tmp.sort()
    num1, num2, num3 = map(int, tmp)
    if num1 == num2 and num2==num3:
        reward=10000 + num1*1000
    elif num1==num2 and num1!=num3:
        reward=1000 + num1*100
    elif num1==num3 and num1!=num2:
        reward = 1000 + num1 * 100
    elif num2==num3 and num1!=num2:
        reward = 1000 + num2 * 100
    reward_list.append(reward)


reward_list.sort(reverse=True)

print(reward_list[0])



