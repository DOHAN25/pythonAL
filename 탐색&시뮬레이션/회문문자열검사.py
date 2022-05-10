
num = int(input("N을 입력해 주세요: "))
answer = []
for i in range(num):
    input_str = input("문자열을 입력해주세요: ")
    input_str=input_str.upper()
    size=len(input_str)
    for j in range(size//2):
        if input_str[j]!=input_str[-1-j]:
            answer.append("No")
            print("#%d No" %(i+1))
            break
    else:
        print("#%d Yes" %(i+1))



# 다른 방법
for i in range(num):
    input_str = input("문자열을 입력해주세요: ")
    input_str=input_str.upper()
    size=len(input_str)
    if input_str==input_str[::-1]:
        print("%d Yes" %(i+1))
    else:
        print("%d No" %(i+1))



