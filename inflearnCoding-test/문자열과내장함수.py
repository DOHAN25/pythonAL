


msg = "It is time"

print(msg.upper())
# 원본은 그대로 있다.
print(msg)
print(msg.lower())


tmp = msg.upper()
print(tmp.find("T"))
# find 함수 = 인덱스를 찾아준다.

print(tmp.count('T'))
# count함수 갯수를 찾아준다.

print(msg[:2])
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i])

print()

for x in msg:
    print(x, end='')
print()

for x in msg:
    if x.isupper():
        print(x, end='')

print()

for x in msg:
    if x.islower():
        print(x, end='')
print()

for x in msg:
    if x.isalpha():
        print(x, end='')

print()



# ord 아스키넘버 알려준다. A : 65 / Z : 90
tmp = 'AZ'

for x in tmp:
    print(ord(x))

# a : 97 / z : 122
tmp = 'az'
for x in tmp:
    print(ord(x))
print()

# 아스키 넘버값은 문자로 변경해주기
tmp = 65
print(chr(tmp))