import os
import msvcrt

definicje = {}

while True:
    print("+--=======-Menu-=======--+ \n"
          "1.Dodaj nowa definicje \n"
          "2.Szukaj definicji \n"
          "3.Usuń definicje \n"
          "4.Pokaż słownik definicje \n"
          "5.Wyjdź")
    while True:
        if msvcrt.kbhit():
            wybor = msvcrt.getch().decode('utf-8')
            break
    
    if wybor == "1":
        os.system('clear')
        klucz = input("Podaj klucz do definicji:")
        if klucz in definicje:
            print("Taki klucz już istnieje! Podaj inna nazweklucza i spróbuj jeszcze raz\n"
                  "Podaj inna nazwe klucza i spróbuj jeszcze raz\n")
            print("\n")

        else:
            definicja = input("Podaj defnicje:")
            definicje[klucz] = definicja
            os.system('clear')
       
    elif wybor == "2":
        os.system('clear')
        szukaj = input("Podaj klucz:")
        klucz = szukaj
        if szukaj in definicje:
            print("Oto definicja:", definicje[szukaj])
        else:
            os.system('clear')
            print("Dany klucz nie ma definicji!")
            print("\n")

    elif wybor == "3":
        os.system('clear')
        usun = input("Podaj klucz:")
        if usun in definicje:
            print("Kod usuwanej definicji",usun ,"oraz, usunieta definicja:", definicje[usun])
            print("\n")
            del definicje[usun]
        else:
             os.system('clear')
             print("Podany klucz nie ma definicji!\n")

    elif wybor == "4":
        os.system('clear')
        print(definicje)
        print("\n")

    elif wybor == "5":
       break
    else:
        os.system('clear')
        print("Podana zła liczba!\n")
        




    