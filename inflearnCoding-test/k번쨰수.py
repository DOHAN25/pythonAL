

T = int(input())

for t in range(T):
    n, s, e, k = map(int,input().split())
    input_list = list(map(int, input().split()))
    input_list = input_list[s-1:e]
    input_list.sort()
    print("#%d %d" %(t+1, input_list[k-1]))