
lista = [1, 5, -23 , -34, -5, 3, 6, 105, 342, -342, 53]

def dodawanieListy(liczby):
        suma = 0
        for liczba in liczby:
          if (liczba > 0):
            suma += liczba 
        return suma


print(dodawanieListy(lista))