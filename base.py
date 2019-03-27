import pandas as pd
import time
from tqdm import tqdm, trange

#df = pd.read_csv("https://docs.google.com/spreadsheets/u/0/d/1x0EzBMIOnFpyCPbO_vfW3ZZxFEfQyr5u7avzaCVMPXs/export?format=csv")

availableClasses = ["Warrior", "Mage", "Druid", "Warlock", "Paladin", "Priest", "Hunter", "Shaman", "Rogue"]
PlayerDict = {}

class Player:
    def __init__(self, name, heroClass):
        self.name = name
        self.heroClass = heroClass

while True:
    try:
        nrPlayers = int(input("Number of Players: "))
        break
    except ValueError:
        print("oops, that was not a correct number. Try again")

print("I see, I see.... {} poor souls decided to enter the evil realm and the home of foul creatures. Beware, for your life is in great danger.".format(nrPlayers))
print("Now, each of you has to introduce himself with his name and class. The following classes are available:")

time.sleep(1.5)

print("---")
for item in availableClasses:
    print(item)
print("---")


for i in range(nrPlayers):
    trash_name = input("Player {}, state your name: ".format(i+1))
    trash_class = input("Oh mighty {}, what class do you wish to play? Chose from the list above: ".format(trash_name))
    while True:
        if trash_class in availableClasses:
            break
        else:
            print("{} is not a valid class name! Reconsider your life choices!".format(trash_class))
            time.sleep(0.5)
            trash_class = input("Now tell me, peasant, what class do you wish to play?: ".format(trash_name))
    PlayerDict.update({i + 1 : Player(trash_name, trash_class)})
    if i + 1 != nrPlayers:
        time.sleep(0.5)
        print("So {} it is! Next Adventurer!".format(trash_class))
    else:
        time.sleep(0.5)
        print("So {} it is!".format(trash_class))

time.sleep(0.5)

print("")
print("Hurraaaaay, the group is assembled. Here is a summary:")

for key, value in PlayerDict.items():
    print("Player {}: {} as a {}".format(key,value.name, value.heroClass))

