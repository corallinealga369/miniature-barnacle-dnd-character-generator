#! python3
import random
import time
import csv
#import pygame
#I want to store the randomly generated stats
#for a character in a dictionary

#These are the default stats for the character
#we are initializing values
#If the stat is zero you know there was an issue
Strength=0
Dexterity=0
Constitution=0
Intelligence=0
Wisdom=0
Charisma=0
MyRace="Human"
MyGender="Woman"
Age=21
LifeStage="Adult"

Race=["Dwarf","Gnome","Dragonborn", "Half-Elf","Teifling","Half-Orc","Halfling","Elf","Human"]
Gender=["Man","Woman"]
LifeStage=["Child", "Adult","Elderly"]

print("Welcome!")
print('Let\'s generate base stats for your character.')
Name=input("First things first, what is your character's name?")
time.sleep(2)
print("Let's pick their gender. Hit Enter")
MyGender=random.choice(Gender)
time.sleep(2)
print("What is your character's race? Hit enter to find out! ")
time.sleep(2)
MyRace=random.choice(Race)
print("What is your character's age? Let's roll for it! ")
time.sleep(2)

if MyRace="Human":
    Age=random.randint(6,90)
    if Age < 18
    LifeStage=Child
    elif Age > 65
    LifeStage=Elderly
    else LifeStage=Adult
elif MyRace="Dwarf":
    Age=random.randint(6,350)
    if Age < 18
    LifeStage=Child
    elif Age > 200
    LifeStage=Elderly
    else LifeStage=Adult
elif MyRace="Halfling":
    Age=random.randint(6,250)
    if Age < 20
    LifeStage=Child
    elif Age > 150
    LifeStage=Elderly
    else LifeStage=Adult
elif MyRace="Elf":
    Age=random.randint(6,750)
    if Age < 100
    LifeStage=Child
    elif Age > 650
    LifeStage=Elderly
    else LifeStage=Adult    
elif MyRace="Dragonborn":
    Age=random.randint(1,80)
    if Age < 15
    LifeStage=Child
    elif Age > 65
    LifeStage=Elderly
    else LifeStage=Adult  
elif MyRace="Gnome":
    Age=random.randint(6,20)
    if Age < 20
    LifeStage=Child
    elif Age > 200
    LifeStage=Elderly
    else LifeStage=Adult 
elif MyRace="Half-Elf":
    Age=random.randint(6,180)
    if Age < 20
    LifeStage=Child
    elif Age > 150
    LifeStage=Elderly
    else LifeStage=Adult    
elif MyRace="Half-Orc":
    Age=random.randint(6,75)
    if Age < 14
    LifeStage=Child
    elif Age > 60
    LifeStage=Elderly
    else LifeStage=Adult   
elif MyRace="Teifling":
    Age=random.randint(6,100)
    if Age < 18
    LifeStage=Child
    elif Age > 70
    LifeStage=Elderly
    else LifeStage=Adult  

print("So your character "+Name+" is a "+Age+" year old "+LifeStage+" "+Race+" "+MyGender+"." ) 
time.sleep(2)   
print("Great, let's roll your stats.")

Strength=random.randint(1,20)
Dexterity=random.randint(1,20)
Constitution=random.randint(1,20)
Intelligence=random.randint(1,20)
Wisdom=random.randint(1,20)
Charisma=random.randint(1,20)
#establish a dictionary for the character stats
mycharacter = {
     "Name":Name,
     "Race":MyRace,
     "Gender":MyGender,
     "Age":Age,
     "Life Stage":LifeStage,
     "Strength":Strength,
     "Dexterity":Dexterity,
     "Constitution":Constitution,
     "Intelligence":Intelligence,
     "Wisdom":Wisdom,
     "Charisma":Charisma,
}
time.sleep(2)
print("Here are the stats for your character")
for key, value in mycharacter.items():
    print(f"{key}:{value}")

f = open("mycharacter.txt","w")
f.write( str(mycharacter) )
f.close()

w = csv.writer(open( "mycharacter.csv", "w"))
for key, val in mycharacter.items():
    w.writerow([key, val])
print("You now have a text file and csv with your character stats!")
print("You can open the csv in Excel or Google Docs.")

time.sleep(2)
print("Bye!")
