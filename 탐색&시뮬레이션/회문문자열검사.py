
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






'''
회문 문자열 
n개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면 Yes
를 출력하고 회문 문자열이 아니면 No를 출력하는 프로그램을 작성하여라.
단 회문을 검사할때 대소문자를 구분하지 않는다.
'''

n=int(input("n:"))
for i in range(n):
    str=input("회문 문자열?:")
    str.upper()
    for j in range(len(str)//2):
        if str[j]!=str[-1-j]:
            print("%d No", %(i+1))
            break
    else:
        print("%d Yes", %(i+1))
