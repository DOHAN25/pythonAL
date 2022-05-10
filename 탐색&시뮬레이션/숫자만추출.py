

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


# 다른 풀이법
# isdecimal : 0~9까지의 숫자인지 확인해준다 포함되면 : True
for x in input_str:
    if x.isdecimal():
        res=res*10+int(x)

print(x)

cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)