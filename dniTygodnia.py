from enum import IntEnum

Menu_Tydzien = IntEnum('Menu_Tydzien', ('Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek'))
print(list(Menu_Tydzien))
wybor = int(input(""" 
1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek

"""))

if(wybor == Menu_Tydzien.Poniedziałek):
    print("Poniedziałek lypa")
if(wybor == Menu_Tydzien.Wtorek):
    print("Wtorek lypa")
if(wybor == Menu_Tydzien.Środa):
    print("Środa lypa")
if(wybor == Menu_Tydzien.Czwartek):
    print("Czwartek lypa")
if(wybor == Menu_Tydzien.Piątek):
    print("Piątek lypa")