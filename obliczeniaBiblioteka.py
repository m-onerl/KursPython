import figury
import os

from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', {'Kwadrat' : 4, 'Prostokąt' : 43, 'Trójkąt' : 7, 'Trapez' : 12, 'Koło' : 1})
print(list(Menu_Figury))
while True:
    wybor = int(input("""\n
    Menu:\n
1.Pole kwadratu
2.Pole prostokat
3.Pole trojkat
4.Pole trapez
5.Pole kola\n"""

        ))
    
    if (wybor == Menu_Figury.Kwadrat):
        os.system("clear")
        a = float(input("a: "))
        x = figury.kwadrat(a)
        print("Pole =", x)

    elif (wybor == Menu_Figury.Prostokąt):
        os.system("clear")
        a = float(input("a: "))
        b = float(input("b: "))
        x = figury.prostokat(a, b)
        print("Pole =", x)

    elif (wybor == Menu_Figury.Trójkąt):
        os.system("clear")
        a = float(input("a: "))
        h = float(input("h: "))
        x = figury.trojkat(a, h)
        print("Pole =", x)

    elif (wybor == Menu_Figury.Trapez):
        os.system("clear")
        a = float(input("a: "))
        b = float(input("b: "))
        h = float(input("h: "))
        x = figury.trapez(a, b, h)
        print("Pole =", x)

    elif (wybor == Menu_Figury.Koło):
        os.system("clear")
        r = float(input("r: "))
        x = figury.kolo(r)
        print("Pole =", x)





