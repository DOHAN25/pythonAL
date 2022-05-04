import math
students = int(input())

students_grade = list(map(int, input().split()))

ave = int(sum(students_grade)/students + 0.5)

min = float('inf')


for idx, x in enumerate(students_grade):
    tmp = abs(x-ave) # 절대값으로
    if tmp < min:
        min = tmp
        socre = x
        res = idx + 1
    elif tmp == min:
        if x > socre:
            score = x
            res = idx + 1


print(ave, res)


