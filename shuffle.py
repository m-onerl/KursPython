

import random

cardList = ["9", "9", "9", "9",
            "10", "10","10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

rekaGracza1 = []
rekaGracza2 = []

def losowanie_kart(gracz, ilosc):
    random.shuffle(cardList)
    x = 0
    while ilosc > x:
        x += 1
        karta = cardList.pop()
        gracz.append(karta)
    print(gracz)

losowanie_kart(rekaGracza1, 6)
losowanie_kart(rekaGracza2, 6)
"""def Lotto(amount, total):
    wylosowane = []
    x = 0
    while x < amount:
        x = x + 1
        liczba_losowa = random.randint(1, total)
        if liczba_losowa not in wylosowane:
            wylosowane.append(liczba_losowa)
    print(wylosowane)
        

Lotto(6, 49)"""

"""def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

choose_random_numbers(6, 49)
"""