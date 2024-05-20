import time

def sumujDo(liczba):
    suma = 0

    for liczba in range(1, liczba + 1):
        suma += liczba
    return suma

def sumujDo2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])

def sumujDo3(liczba):
    return sum((liczba for liczba in range(1, liczba+1)))

def sumujDo4(liczba):
    return sum({liczba for liczba in range(1, liczba+1)})

def sumujDo5(liczba):
    return(1 + liczba) / 2 * liczba

def finishTimer(start):
    end = time.perf_counter()
    return end - start




def functionPerformance(func, arg, howMany = 1):
    sum = 0
    for i in range(0, howMany):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum += (end - start)
    return sum

def showMess(message):
    print(message)

print(functionPerformance(sumujDo, 5000000))
print(functionPerformance(sumujDo2, 5000000))
print(functionPerformance(sumujDo3, 5000000))
print(functionPerformance(sumujDo4, 5000000))
print(functionPerformance(sumujDo5, 5000000))
