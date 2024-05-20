import copy


def devil_function(list):
    print(id(list))
    print(list)
 

listDestroyed = [3, 5, 6, 30, 100, 30]
print(listDestroyed)

print(id(listDestroyed))
devil_function(listDestroyed[:])



