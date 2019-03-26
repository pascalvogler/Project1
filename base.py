import pandas as pd
import sys

#df = pd.read_csv("https://docs.google.com/spreadsheets/u/0/d/1x0EzBMIOnFpyCPbO_vfW3ZZxFEfQyr5u7avzaCVMPXs/export?format=csv")

availableClasses = ["Warrior", "Mage", "Druid", "Warlock", "Paladin", "Priest", "Hunter", "Shaman", "Rogue"]
PlayerList = []

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

for i in range(nrPlayers):
    trash_name = input("Player {}, state your name: ".format(i+1))
    trash_class = input("Oh mighty {}, what class do you wish to play?: ".format(trash_name))