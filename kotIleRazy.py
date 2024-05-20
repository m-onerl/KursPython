word = "kot"
path = "plik.txt"

def findWord(plik, kot):
    try:
        with open(plik, "r", encoding="UTF-8") as file:
            text = file.read()
            calculate = text.count(kot)
            return print(f"Słowo {word} znajduje sie w {path} tyle razy: {calculate} ")
        
    except FileNotFoundError:
            print(f"Plik o nazwie '{plik}' nie istnieje!")

findWord(path, word)
