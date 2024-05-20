
names = {"Sebastian", "anna", "Konrad", "tymoteusz", "Łucja", "mateusz"}

names = {name.capitalize()
         for name in names
         if not name.startswith("t" or "T")
         }


print(names)