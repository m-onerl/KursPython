with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        dane = file.readline().strip().split()
   
        imie, nazwisko = dane[0], ' '.join(dane[1:])
       
        with open("imie.txt", "a") as imie_file:
                imie_file.write(imie, '/n')

        with open("nazwisko.txt", "a") as nazwisko_file:
                nazwisko_file.write(nazwisko, '/n')

        