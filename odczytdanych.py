"""
json.loads(jsonstring) - przetwarza jsonstring na dane typu Python

json.load(filePointer) - wczytuje jeden z pliku i zwraca jako wynik metody dane typu Python


"""

film = {
    "title" : "Ale ja nie będe tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors" : ("John Doe", "Jane Doe"),
    "budget" : None,
    "credits" : {
        "director" : "John Doe",
        "scenarist" : "Jane Doe",
        "cameraman" : "Alfred Hitchcock"
    }

}
import json

encodedRetrievedMovie = '{"title" : "Ale ja nie będe tego robił!", "release_year" : 1969, "won_oscar" : true, "actors" : ["John Doe", "Jane Doe"], "budget" : null, "credits" : {"director" : "John Doe", "scenarist" : "Jane Doe", "cameraman" : "Alfred Hitchcock"}}'

decodedMovie = json.loads(encodedRetrievedMovie)
with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)
    
print(decodedMovie)