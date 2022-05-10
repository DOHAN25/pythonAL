

input_str=input("문자열을입력하세요: ")

str=""

for i in range(len(input_str)):
    if input_str[i].isdigit():
        str+=input_str[i]

str=int(str)

print(str)

cnt=0

for i in range(1, str+1):
    if str%i==0:
        cnt+=1

print(cnt)