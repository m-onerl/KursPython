definicje = {}
 
def dodajDefinicje(klucz, definicja, definicje):
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")


def znajdzDefinicje(klucz, definicje):
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji o nazwie", klucz)

def usunDefinicje(klucz, definicje):
            if klucz in definicje:
                del definicje[klucz]
                print("Usunięto definicję o nazwie:", klucz)
            else:
                print("Nie znaleziono definicji o nazwie", klucz)

while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Zakończ")
 
    wybor = input("Co chcesz zrobić? ")
 
    if (wybor == "1"):
        klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        dodajDefinicje(klucz, definicja, definicje)

    elif (wybor == "2"):
        klucz = input("Czego szukasz? ")
        znajdzDefinicje(klucz, definicje)
    elif (wybor == "3"):
        klucz = input("Jaką definicję chcesz usunąć? ")
        usunDefinicje(klucz, definicje)
    elif (wybor == "4"):
        print("No to pa!")
        break
    else:
        print("Podałeś coś z poza zakresu")