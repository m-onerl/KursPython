"""
podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:
r+ - do czytania i pisania

file.read file.write

w+ - do pisania i czytania
różni sie tym, że usunie zawartość istniejącego pliku
lub stworzy plik gdy go nie było

a+ - "wieczny tryb" dopisywania i przy okazji czytania
UWAGA! wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istniał - stworzy go

[
("Sebastian", "Wołoszyn")
]
"""
namesandsurnames = []

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesandsurnames.append(tuple(line.replace("\n", "").split(" ")))

  
with open("imiona.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurnames:
        file.write(item [0] + "\n")

with open("nazwiska.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurnames:
        try:
            file.write(item [1] + "\n")
        except IndexError:
            file.write("\n")
