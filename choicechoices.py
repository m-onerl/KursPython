
import random

movieList = ["Diuna", "Las Vegas Parano", "Pulp Fiction", "Fight Club", "Intelstelar"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata przedmiotów"]

lootZeSkrzyni = ["normalna", "średnia", "dobra", "wysoka", "legendarna"]

from collections import Counter
print(Counter(random.choices(lootZeSkrzyni, weights = [0.9, 0.8, 0.5, 0.05, 0.01], k = 100)))

