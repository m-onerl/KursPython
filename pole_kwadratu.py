import os

def kwadrat(a):
    return a * a

def prostokat(a, b):
    return a * b

def trojkat(a, h):

    return (1/2 * (a * h))

def trapez(a, b, h):

    return (((a + b) * h) * 1/2)

def kolo(r):
    z = 3.14
    u = r ** 2
    return (z * u)

while True:
    print("\n"
        "Menu:\n"
        "1.Pole kwadratu\n"
        "2.Pole prostokat\n"
        "3.Pole trojkat\n"
        "4.Pole trapez\n"
        "5.Pole kola"

        )
    wybor = input()

    if wybor == "1":
        os.system("clear")
        a = int(input("a: "))
        x = kwadrat(a)
        print("Pole = ", x)

    elif wybor == "2":
        os.system("clear")
        a = int(input("a: "))
        b = int(input("b: "))
        x = prostokat(a, b)
        print("Pole = ", x)

    elif wybor == "3":
        os.system("clear")
        a = int(input("a: "))
        h = int(input("h: "))
        x = trojkat(a, h)
        print("Pole = ", x)

    elif wybor == "4":
        os.system("clear")
        a = int(input("a: "))
        b = int(input("b: "))
        h = int(input("h: "))
        x = trapez(a, b, h)
        print("Pole = ", x)

    elif wybor == "5":
        os.system("clear")
        r = int(input("r: "))
        x = kolo(r)
        print("Pole = ", x)

    else:
        break







