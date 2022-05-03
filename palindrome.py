# 주어진 문자열이 팰린드롬인지 확인하여라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 입력 : 'A man, a plan, a canal: Panama'
# 출 : true

# 입력 : 'race a car'
# 출력 : false

s = input("문자열을 입력해 주세요: ")
strs = []

for char in s:
    if char.isalnum():
        strs.append(char.lower())
print(strs)
result = 'True'
while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        result = 'False'
        break

print(result)


