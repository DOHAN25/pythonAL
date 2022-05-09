

num_list=list(input("숫자를 입력해주세요. : ").split())


def reverse(list):
    reverse_num_list=[]
    for x in list:
        reverse_num_list.append(int(x[::-1]))
    return reverse_num_list

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True



for x in reverse(num_list):
    if isPrime(x):
        print(x, end=" ")

