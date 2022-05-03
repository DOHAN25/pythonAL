# 각 자리가 숫자(0부터9)로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를
# 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.

input_num = input()

first_input_num = int(input_num[0])

for i in range(1, len(input_num)):
    num = int(input_num[i])
    if first_input_num <= 1 or num <= 1:
        first_input_num += num
    else:
        first_input_num *= num


print(first_input_num)



