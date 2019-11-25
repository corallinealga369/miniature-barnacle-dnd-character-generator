#! python3
import random
import time
import csv
#import pygame
#I want to store the randomly generated stats
#for a character in a dictionary
Name="Jane Doe"
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
MySize="Medium"
#traits asigned by race or influenced by it
Alignment=["Lawful-Good","Lawful-Nuetral","Lawful-Evil","Neutral-Good","Neutral-Nuetral","Neutral-Evil","Chaotic-Good","Chaotic-Neutral","Chaotic-Evil"]
Gender=["Man","Woman"]
MyRaceNotes="Racial Notes Filler"
Size="Medium"
Speed=25
Age=21
MyLifeStage="Adult"
Height=50
#MyTool="Filler"
Race=["Dwarf","Gnome","Dragonborn", "Half-Elf","Teifling","Half-Orc","Halfling","Elf","Human"]
LifeStage=["Child", "Adult","Elderly"]



#We will generate the stats before doing anything else so that racial bonusus are auto-added
#for example, dwarves get +2 constitution
Strength=random.randint(1,20)
Dexterity=random.randint(1,20)
Constitution=random.randint(1,20)
Intelligence=random.randint(1,20)
Wisdom=random.randint(1,20)
Charisma=random.randint(1,20)

print("Welcome!")
print('Let\'s generate base stats for your character.')
Name=input("First things first, what is your character's name?")
time.sleep(2)
print("Choosing a random alignment for "+Name+".")
MyAlignment=random.choice(Alignment)
print("Generating a gender...")
MyGender=random.choice(Gender)
time.sleep(2)
print("Choosing a race... ")
time.sleep(2)
MyRace=random.choice(Race)
print("Picking an age... ")
time.sleep(2)

#classes
class Dwarf:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    ToolProf=["Smithing","Brewing","Masonry"]
    self.MyTool= random.choice(ToolProf)

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    #Dwarf bonus
    Constitution=Constitution+2
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)
class Human:
  def __init__(self, name ):
    self.name = Name
    self.Size="Medium"
    self.Speed=30
    Height=random.randint(52,75)
    self.Height=Height
    Age=random.randint(6,90)
    self.Age=Age 

    #Human Bonus is +1 all ability
    Strength=random.randint(1,20)
    Strength=Strength+1
    Dexterity=random.randint(1,20)
    Dexterity=Dexterity+1
    Constitution=random.randint(1,20)
    Constitution=Constitution+1
    Intelligence=random.randint(1,20)
    Intelligence=+1
    Wisdom=random.randint(1,20)
    Wisdom=+1
    Charisma=random.randint(1,20)
    Charisma=+1

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.name)
  def stats(self):
    print("Hello my name is " + self.name)
class Halfling:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    
    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

class Elf:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

class Dragonborn:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

class Gnome:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

class HalfElf:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

class HalfOrc:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

class Teifling:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Medium"
    self.Speed=25
    Height=random.randint(40,60)
    self.Height=Height
    Age=random.randint(6,350)
    self.Age=Age 

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Constitution=random.randint(1,20)
    Intelligence=random.randint(1,20)
    Wisdom=random.randint(1,20)
    Charisma=random.randint(1,20)

    self.Strength=Strength
    self.Dexterity=Dexterity
    self.Constitution=Constitution
    self.Intelligence=Intelligence
    self.Wisdom=Wisdom
    self.Charisma=Charisma
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Hello my name is " + self.Name)

if MyRace=="Human":
    
    MyRaceNotes="Humans have no particular alignment tendency. They get +1 to all abilities and get an additional language."
    
    if Age < 18:
        MyLifeStage="Child"
    elif Age > 65:
        MyLifeStage="Elderly"
    else: 
        MyLifeStage="Adult"

elif MyRace=="Dwarf":
    
    MyRaceNotes="Dwarves get +2 to constitution (already added). And are usually lawful.Speed isn't impacted by heavy armor."
    if Age < 18:
        MyLifeStage="Child"
    elif Age > 200:
        MyLifeStage="Elderly"
    else:
        MyLifeStage="Adult"

elif MyRace=="Halfling":
    #We choose some racially influenced traits here
    Age=random.randint(6,250)
    MySize="Small"
    MySpeed=25
    Height=random.randint(30,42)
    MyRaceNotes="Halflings tend to be lawful good. They get a +2 to Dexterity.They are fluent and literate in Common and Halfling."
    Dexterity=Dexterity+2
    #we determine what life stage this makes the being based on their race
    if Age < 20:
        MyLifeStage="Child"
    elif Age > 150:
        MyLifeStage="Elderly"
    else: 
        MyLifeStage="Adult"

elif MyRace=="Elf":
    Age=random.randint(6,750)
    MySize="Medium"
    MySpeed=30
    Height=random.randint(60,72)
    MyRaceNotes="Elves value freedom, and lean towards the gentler aspects of chaos. They get a +2 Dexterity bonus."
    Dexterity=Dexterity+2
    if Age < 100:
        MyLifeStage="Child"
    elif Age > 650:
        MyLifeStage="Elderly"
    else:
        MyLifeStage="Adult"    

elif MyRace=="Dragonborn":
    Age=random.randint(1,80)
    #this race needs an update to their racial traits other than age
    #this filler was placed so functionality could be tested
    MySize="Medium"
    MySpeed=30
    Height=random.randint(60,72)
    MyRaceNotes=" Dragonborn Races Notes"
    if Age < 15:
        MyLifeStage="Child"
    elif Age > 65:
        MyLifeStage="Elderly"
    else:
        MyLifeStage="Adult"  

elif MyRace=="Gnome":
    Age=random.randint(6,20)
    #this race needs an update to their racial traits other than age
    #this filler was placed so functionality could be tested
    MySize="Medium"
    MySpeed=30
    Height=random.randint(60,72)
    MyRaceNotes=" Gnome Race Notes"
    if Age < 20:
        MyLifeStage="Child"
    elif Age > 200:
        MyLifeStage="Elderly"
    else:
        MyLifeStage="Adult" 

elif MyRace=="Half-Elf":
    Age=random.randint(6,180)
    #this race needs an update to their racial traits other than age
    #this filler was placed so functionality could be tested
    MySize="Medium"
    MySpeed=30
    Height=random.randint(60,72)
    MyRaceNotes=" Race"
    if Age < 20:
        MyLifeStage="Child"
    elif Age > 150:
         MyLifeStage="Elderly"
    else: 
        MyLifeStage="Adult"    

elif MyRace=="Half-Orc":
    Age=random.randint(6,75)
    #this race needs an update to their racial traits other than age
    #this filler was placed so functionality could be tested
    MySize="Medium"
    MySpeed=30
    Height=random.randint(60,72)
    MyRaceNotes=" Half Orc Race Notes"
    if Age < 14:
        MyLifeStage="Child"
    elif Age > 60:
        MyLifeStage="Elderly"
    else: 
        MyLifeStage="Adult"   

elif MyRace=="Teifling":
    Age=random.randint(6,100)
    #this race needs an update to their racial traits other than age
    #this filler was placed so functionality could be tested
    MySize="Medium"
    MySpeed=30
    Height=random.randint(60,72)
    MyRaceNotes=" Teifling Race Notes"
    if Age < 18:
        MyLifeStage="Child"
    elif Age > 70:
        MyLifeStage="Elderly"
    else:
         MyLifeStage="Adult"  

#Here is the dictionary we store values in
#establish a dictionary for the character stats
mycharacter = {
     "Name":Name,
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
     #"Tool Proficiency":MyTool,
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
f = open("mycharacter.txt","w")
f.write( str(mycharacter) )
f.close()

#This creates a comma seperated value file
w = csv.writer(open( "mycharacter.csv", "w"))
for key, val in mycharacter.items():
    w.writerow([key, val])
print("You now have a text file and csv with your character stats!")
print("You can open the csv in Excel or Google Docs.")

time.sleep(2)
print("Bye!")
