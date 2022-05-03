
'''
for i in range(5):
    for j in range(4):
        print(j, end=" ")
    print(i)'''

for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()