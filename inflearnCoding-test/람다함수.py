



# 람다 함수 = 익명의 함수 = 람다 표현식

def plus_one(x):
    return x + 1

#print(plus_one(1))

#위에거 람다 함수로 해보자
plus_two = lambda x: x+2

#print(plus_two(1))

# 람다 함수는 어떤 내장함수의 인자로 사용할때 편리하다
a = [1, 2, 3]
print(list(map(plus_one, a)))

# map(함수명, 자료)

# 이럴때 유용하다.
print(list(map(lambda x: x+1, a)))
