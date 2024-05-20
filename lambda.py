
def podwoj(x):
    return x * 2


def funkcja_dla_przefiltruj(x):
    if (x % 2) == 0:
        return x



myList = [2, 14, 5, 76, 1, 23, 132, 54]

myList_filtered1 = list(filter(lambda x: x % 2 == 0, myList)) 
myList_filtered2 = list(filter(funkcja_dla_przefiltruj, myList))  
myList_filtered3 = [x for x in myList if (x % 2 == 0 )  ]
print(myList_filtered1)
  


#test = lambda x: x * 2

#print((lambda x: x * 2)(4))


"""parzysteLiczby = [element
                  for element in myList
                  if (element % 2 == 0 )
]
print(parzysteLiczby)"""