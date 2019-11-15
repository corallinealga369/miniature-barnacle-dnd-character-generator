#! python 3
#Random Dwarf Generator
#! python3
import random
import time
import csv
#import pygame
#I want to store the randomly generated stats
#for a character in a dictionary
Name="Jane"
ClanName="Doe"
#These are the default stats for the character
#we are initializing values
#If the stat is zero you know there was an issue
Strength=0
Dexterity=0
Constitution=0
Intelligence=0
Wisdom=0
Charisma=0
MyRace="Dwarf"
MyGender="Female"
MySize="Medium"
#traits asigned by race or influenced by it
Alignment=["Lawful-Good","Lawful-Nuetral","Lawful-Evil","Neutral-Good","Neutral-Nuetral","Neutral-Evil","Chaotic-Good","Chaotic-Neutral","Chaotic-Evil"]
Gender=["Male","Female"]
MyRaceNotes="Racial Notes Filler"
Size="Medium"
Speed=25
Age=21
MyLifeStage="Adult"
Height=50
MyTool="Filler"
Race=["Dwarf","Gnome","Dragonborn", "Half-Elf","Teifling","Half-Orc","Halfling","Elf","Human"]
LifeStage=["Child", "Adult","Elderly"]
MaleNames=['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak']
FemaleNames=['Eldeth', 'Falkrunn', 'Finellen', 'Gunnloda', 'Gurdis', 'Helja', 'Hlin'] 
ClanNames=['Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil', 'Fireforge', 'Frostbeard', 'Gorunn']




#We will generate the stats before doing anything else so that racial bonusus are auto-added
#for example, dwarves get +2 constitution
Strength=random.randint(1,20)
Dexterity=random.randint(1,20)
Constitution=random.randint(1,20)
Intelligence=random.randint(1,20)
Wisdom=random.randint(1,20)
Charisma=random.randint(1,20)

print("Welcome!")
print('Let\'s a dwarf.')

time.sleep(2)
print("Choosing a random alignment for "+Name+".")
MyAlignment=random.choice(Alignment)
print("Generating a gender...")
MyGender=random.choice(Gender)
if MyGender=="Female":
    Name=random.choice(FemaleNames)
else:
    Name=random.choice(MaleNames)
ClanName=random.choice(ClanNames)        
time.sleep(2)

MyRace="Dwarf"

#dwarves are medium
MySize="Medium"
#dwarves get a racil bonus to constitution
Constitution=Constitution+2
#dwarves base walk speed is 25
MySpeed=25
#dwarves get proficiency in one of the following three tools
ToolProf=["Smithing","Brewing","Masonry"]
MyTool=random.choice(ToolProf)
#dwarves are between 4-5 feet tall
Height=random.randint(40,60)
MyRaceNotes="Dwarves get +2 to constitution (already added). And are usually lawful.Speed isn't impacted by heavy armor."    
Age=random.randint(6,350)
if Age < 18:
    MyLifeStage="Child"
elif Age > 200:
    MyLifeStage="Elderly"
else:
    MyLifeStage="Adult"

#Here is the dictionary we store values in
#establish a dictionary for the character stats
mycharacter = {
     "Name":Name+" "+ClanName,
     "Aligned":MyAlignment,
     "Race":MyRace,
     "Gender":MyGender,
     "Age":Age,
     "Height":Height,
     "Life Stage":MyLifeStage,
     "Size":Size,
     "Strength":Strength,
     "Dexterity":Dexterity,
     "Constitution":Constitution,
     "Intelligence":Intelligence,
     "Wisdom":Wisdom,
     "Charisma":Charisma,
     "Tool Proficiency":MyTool,
     "Racial Notes":MyRaceNotes,
}
print("\n")
print("So your character "+Name+" is a "+MyAlignment+" "+str(Age)+" year old "+MyLifeStage+" "+MyRace+" "+MyGender+"." ) 
print("Their size is "+MySize+" their speed is "+str(MySpeed)+" and their height is "+str(Height)+" inches.")
print("\n")
#print("They have proficiency in "+MyTool+" tools.")
print("And there is a note here about their race:")
print(MyRaceNotes)
time.sleep(2)   


#This will print all the values for the character that are included in the dictionary
time.sleep(2)
print("Here are the stats and notes for your character")
print("\n")
for key, value in mycharacter.items():
    print(f"{key}:{value}")
print("\n")
#this creates a raw text file.
#f = open("mycharacter.txt","w")
#f.write( str(mycharacter) )
#f.close()

#This creates a comma seperated value file
w = csv.writer(open( "mycharacter.csv", "w"))
for key, val in mycharacter.items():
    w.writerow([key, val])
print("You now have a text file and csv with your character stats!")
print("You can open the csv in Excel or Google Docs.")

time.sleep(2)
print("Bye!")