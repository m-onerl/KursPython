import random



def will_weapon_hit(weaponChance):
    hitChance = random.uniform(0, 100)
    if (hitChance < weaponChance):
        return "Hit!"
    return "Miss"



x = 0
listHit = []

while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(70))

from collections import Counter

dictonaryHit = Counter(listHit)

print(dictonaryHit)
 
x = 0
while x < 100:
    x = x + 1
    print(random.randint(0, 10))