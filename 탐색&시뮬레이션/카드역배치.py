

card = list(range(21))

for _ in range(10):
    a, b = map(int, input("a와b를 입력하세요:").split())
    for i in range((b-a+1)//2):
        card[a+i], card[b-i] = card[b-i], card[a+i]

card.pop(0)
print(card)