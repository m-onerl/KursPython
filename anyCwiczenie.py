"""
numbers1 = [1, 3 ,5 ,6 ,7]
numbers2 = [1, 3 ,5 ,7 ,9]
numbers3 = [2, 4 ,6 ,8 ,10]

def any_even(lista):
 return any([nr % 2 == 0 for nr in lista])
       
def all_even(lista):
 return all([nr % 2 == 0 for nr in lista])

print(all_even(numbers1))
print(all_even(numbers3))

if(any_even(numbers1)):
    print("parzysta")
else:
    print("nie parzysta")
    """
"""numbers1 = [nr % 2 == 0
    for nr in numbers1
]
numbers2 = [nr % 2 == 0
    for nr in numbers2
]
print(any(numbers1))
print(any(numbers2))
# any - jakikolwiek"""

john = {
    'name': 'John Doe',
    'age' : 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age' : 25,
    'skills': ['Python', 'Java']
}

wantedSkills = ['Python', 'JavaScript']


def recruitmentany(person):
 return any(skill == 'JavaScript' and "Python" for skill in person['skills'])
                

def recruitmentall(person, skills):
 return all(skill in person['skills'] for skill in skills)

print(recruitmentany(john))
print(recruitmentany(jane))

print(recruitmentall(john, wantedSkills))
print(recruitmentall(jane, wantedSkills))