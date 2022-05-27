

'''
9x9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3x3 크기의 보드에 1부터 9까지의
숫자가 중복없이 나타나도록 보드를 채우면 된다.


'''


input_list=[list(map(int, input(":").split())) for _ in range(9)]


check_row = [0]*10
check_column = [0]*10
check_diagnal = [0]*10
result=0

def check_list(list):
    for i in range(9):
        for j in range(9):
            check_row[input_list[i][j]]=1
            check_column[input_list[j][i]]=1
        if sum(check_row)!=9 or sum(check_column)!=9:
            return False
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    check_diagnal[input_list[i*3+x][j*3+y]]=1
            if sum(check_diagnal)!=9:
                return False
    return True

if check_list(input_list):
    print("Yes")
else:
    print("No")