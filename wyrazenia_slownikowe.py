"""Wyrażenia słownikowe"""

names = {"Sebastian", "Anna", "Konrad", "Tymoteusz", "Łucja"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1' : -20, 't2' : 0, 't3' : -4, 't4' : 6, 't5' : 25}
namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}
multipliedNumbers = {
    number : number ** 3
    for number in numbers
}

farenheit = {
    key  : (9/5) * celcius + 32 
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20
}

print(farenheit)
