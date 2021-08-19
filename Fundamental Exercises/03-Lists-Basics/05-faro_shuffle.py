deck = input().split()
number = int(input())
for i in range(number):
    shuffled_deck = []
    for index in range(len(deck)//2):
        first_card = deck[index]
        second_card = deck[len(deck)//2 + index]
        shuffled_deck.append(first_card)
        shuffled_deck.append(second_card)
    deck = shuffled_deck
print(deck)