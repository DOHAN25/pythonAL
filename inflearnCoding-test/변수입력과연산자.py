'''
a = input("숫자를 입력하세요. : ")
print(a)
'''
'''
a, b = input("숫자를 입력해 주세요: ").split()
print(a, b)
print(type(a))
c = a + b
print(c)
print(type(c))
print(a + b) # str값으로 들어오기 때문에 연결된다.
'''

'''
a, b = input("숫자를 입력해 주세요 : ").split()
a = int(a)
b = int(b)
print(type(a))
print(a + b)
'''
'''
# map 내장함수
a, b = map(int, input("숫자를 입력해 주세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 몫
print(a % b) # 나머지
print(a ** b) # 거듭제곱
 
'''

a = 4.3
b = 5
c = a + b
print(type(c))