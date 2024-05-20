
Numbers = [number 
            for number in range(100, 471)
            if (number % 7 == 0 )
            if (number % 5 != 0)
                        
]
generateNumbers = (number 
                for number in range(100, 471)
                if (number % 7 == 0 )
                if (number % 5 != 0)
                        
)
Numbersdict = {number : number / number  
            for number in range(100, 471)
            if (number % 7 == 0 )
            if (number % 5 != 0)
}

print(Numbers)

print(Numbersdict)

for number in generateNumbers:
    print(number)
