'''
a = range(10)
print(list(a))

a = range(1, 11)
print(list(a))
'''
'''
for i in range(10):
    print(i)
'''
'''
for i in range(10, 0, -1):
    print(i)
'''

'''
i = 1
while i <= 10:
    print(i)
    i = i + 1
'''
'''
i = 1
while True:
    print(i)
    i += 1
    if i == 10:
        break
'''

'''
for i in range(1, 11):
    if i%2 == 0:
        continue
    print(i)
'''

for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)


for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)

