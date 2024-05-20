"""try:
        
    file = open("test.txt", "w")
    file.write("sample")
    print (0/0)
    a = 5
    file.write("sample")

finally: 
    file.close()
    a = 5

    print(a)"""

"""with open("test.txt", "w") as file:
    file.write("sample")

    a = 5
    file.write("sample")"""

with open("oceany.txt", "a+", encoding="UTF-8") as file:
    file.write("Wielki ocean")
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("Wielki zielony ocean")
    

"""   
    print(file.readline())
    print(file.tell())
    file.seek(6)
    print(file.tell())
    print(file.readline())
"""
"""for line in file:
        print(line)"""

"""   oceany = file.read().splitlines()
    oceany2 = file.readline()
    oceany3 = file.readlines()
print(oceany)
print(oceany2)"""