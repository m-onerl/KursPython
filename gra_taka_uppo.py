import random
from enum import Enum


def findApproxmiateValue(value, precentRange):
    lowestValue = value - (precentRange / 100) * value
    highestValue = value + (precentRange / 100) * value
    return random.randint(lowestValue, highestValue)

Event = Enum('Event', ['Chest', 'Empty'])
eventDictionary ={
                Event.Chest: 0.6,
                Event.Empty: 0.4
}
eventList = list(eventDictionary.keys())

eventProbability = list(eventDictionary.values())
Colours = Enum('Colours', {'Green' : 'Zielony',
                           'Orange' : 'Pomarańczowy',
                           'Purple' : "Fioletowy",
                           'Gold' : "Złoty"

})
chestColoursDictionary = {
                Colours.Green: 0.75,
                Colours.Orange: 0.2,
                Colours.Purple: 0.04,
                Colours.Gold: 0.01
}
chestColoursList = tuple(chestColoursDictionary.keys())
chestColoursProbability = tuple(chestColoursDictionary.values())

rewardsFromChests = {
                    chestColoursList[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(chestColoursList))
                    

}

gameLength = 5
goldAcquired = 0 
print("Welcome to my game Obciąganie")
print("There you have only 5 moves so its not really estensive but enjoy")

while (gameLength > 0):
    gameAnswer = input("Do you want to move forward?")
    if (gameAnswer == "yes"): 
        print("Yessir, you moved let's see what you got..")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("You get a CHEST")
            drawnColor = random.choices(chestColoursList, chestColoursProbability)[0]
            print("The chest color is", drawnColor.value)
            gamerReward = findApproxmiateValue(rewardsFromChests[drawnColor], 10)
            goldAcquired = goldAcquired + gamerReward
        elif (drawnEvent == Event.Empty):
            print("You are so unlucky, you drawn nothing!")
        
    else:
        print("You can go only straight man, no more option")
        continue

    gameLength = gameLength - 1
print("Congrats you het acquired", goldAcquired)
        