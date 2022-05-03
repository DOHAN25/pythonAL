# 변수란?
# 변수명 정하기
# 1. 영문과 숫자, _ 로 이루어진다.
# 2. 대소문자를 구분한다.
# 3. 문자나, _ 로 시작한다.
# 4. 특수문자를 사용하면 안된다 (&, % 등)
# 5. 키워드를 사용하면 안된다.
'''
여러 줄 주석 하는 방법
'''
a = 1
A = 2
print(a, A)


# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)


# 변수 타입
a = 12345
print(type(a))
a = 12.23123
print(type(a))
a = 'student'
print(type(a))


# 출력방식
print('number')
a, b, c = 1, 2, 3
print(a, b, c)
# seperator 각 변수 사이를 이렇게 바꿔라.
print(a, b, c, sep='')
print(a, b, c, sep=', ')
print(a, b, c, sep='\n')
