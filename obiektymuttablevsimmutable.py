


listSample = [1, 4 ,512 ,24]
#print(id(listSample))

listSample2 = listSample


"""print(listSample2)
print(listSample)
"""

"""k = 4
h = 4
c = 5

print(id(c))
def add(c , ammount = 1):
    print (id(c))
    print(c)
    c = c + ammount
    print(id(c))

add(c)"""

def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))


print(id(listSample))
print(listSample)
append_element_to_list(listSample, 5)


print(listSample)
print(id(listSample))