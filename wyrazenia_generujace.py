import sys

evenNumbers = [element
                        for element in range(10)
                        if (element ** 2 )
]

evenNumberGenerator = (element
                        for element in range(10)
                        if (element  ** 2 )
                        )

for item in evenNumbers:
    print(item)

for item in evenNumberGenerator:
    print(item)  

