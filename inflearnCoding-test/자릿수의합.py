'''
n = int(input('N을 입력해주세요. : '))

input_num_list=list(map(int, input("숫자를 입력해 주세요.: ").split()))

def digit_sum(x):
    sum=0 # 각 합할 값
    while x>0:
       sum+=x%10
       x=x//10
    return sum


result = []
for x in input_num_list:
    tot = digit_sum(x)
    result.append(tot)

print(result)
'''

# 풀이2 문자열로 받아서 문자열 다 더하기
input_str_list=list(input("숫자입력: ").split())
str_result =[]
def digit_str_sum(x):
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    return sum

for x in input_str_list:
    str_result.append(digit_str_sum(x))


print(str_result)




