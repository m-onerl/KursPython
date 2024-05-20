
def readaFile(file):
    try:
        with open(file, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
            print("Plik o nazwie " + file + " nie istnieje!")





fileName = input("Podaj nazwe pliku: ")
fileContent = readaFile(fileName)
print(fileContent)