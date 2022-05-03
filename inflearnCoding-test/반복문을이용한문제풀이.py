# 1) 1부터 N까지의 홀수 출력하기
'''
input_num = input("숫자를 입력해 주세요 : ")
input_num = int(input_num)

for i in range(1, input_num + 1):
    if i % 2 == 0:
        continue
    print(i)
'''
'''
# 2) 1부터 N까지의 합 구하기
input_num = input("숫자를 입력해 주세요 : ")
input_num = int(input_num)
result = 0
for i in range(1, input_num+1):
    result += i


print(result)
'''

# 3) N의 약수출력하기
input_num = input("숫자를 입력해 주세요 : ")
input_num = int(input_num)
list = []
for i in range(1, input_num + 1):
    if input_num % i == 0:
        list.append(i)


print(list)
