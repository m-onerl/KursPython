slownik = {}


while True:
    print("Menu:\n"
        "1.Dodaj do słownika\n"
        "2.Wyszukaj w słowniku\n"
        "3.Usuń klucz z definicja \n"
        "4.Wyświetl slownik\n"
        "5.Zamknij\n")
    wybor = input()
    
    if wybor == "1":
        klucz = input("Podaj klucz: ")
        if klucz in slownik:
                    print("Taki klucz istnieje!\n"
                        "Spróbuj jeszcze raz z innym kluczem") 
        else:
            definicja = input("Podaj definicje: ") 
            slownik[klucz] = definicja

    if wybor == "2":
        klucz = input("Podaj klucz: ")
        if klucz in slownik:
                    print("Oto definicja tego klucza", slownik[klucz])
                         
        else:
            print("Nie ma takiego klucza! ", klucz)

    if wybor == "3":
        klucz = input("Podaj klucz: ")
        if klucz in slownik:
            print("Usunięto ten klucz", slownik[klucz])
            del slownik[klucz]
        else:
            print("Nie ma takiego klucza! ", klucz)

    if wybor == "4":
        print(slownik)

    if wybor == "5":
        break
