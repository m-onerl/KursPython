import time

setContainer = {i for i in range (1, 1001)}
listContainer = [i for i in range (1, 1001)]

def timer(start):
        end = time.perf_counter()
        return print(end - start)

def functionPerformance(func, howMany = 1, *arg): # **arg mozna zdefiniować argumenty z funkcji nazwą danego argumentu
    sum = 0

    for i in range(0, howMany):
        start = time.perf_counter()
        func(*arg) #findNumber = value = 500, container =setContainer
        end = time.perf_counter()
        sum += (end - start)
    return sum

def findNumber(number, container):
    if number in container:
            return True
    else:
            return False


print(functionPerformance(findNumber, 500000, 500,  setContainer))
print(functionPerformance(findNumber, 500000,  500,  listContainer))


#findNumber(300,setContainer)

"""def findNumber(container):
    number = int(input("Sprawdz czy liczba jest w zbiorze:")) 
    if number in container:
            return print(number, "Liczba jest w zbiorze")
    return print(number,"Takiej liczby nie ma w zbiorze ;-;")


functionPerformance(findNumber, listContainer, howMany = 3)
"""
"""start = time.perf_counter()
findNumber(listContainer)
timer(start)

start = time.perf_counter()
findNumber(setContainer)
timer(start)"""

    
