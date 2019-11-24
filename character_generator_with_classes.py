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


print("Welcome!")
print('Let\'s generate base stats for your character.')
Name=input("First things first, what is your character's name?")
time.sleep(2)
print("Choosing a random alignment for "+Name+".")
MyAlignment=random.choice(Alignment)
print("Generating a gender...")
MyGender=random.choice(Gender)


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
    self.Alignment=MyAlignment
    self.Gender=MyGender
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))
    
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
    self.Alignment=MyAlignment
    self.Gender=MyGender
    
    
  def introduce(self):
    print("Hello my name is " + self.name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))
    
class Halfling:
  def __init__(self, Name ):
    self.Name = Name
    self.Size="Small"
    self.Speed=25
    Height=random.randint(30,42)
    self.Height=Height
    Age=random.randint(6,250)
    self.Age=Age 
    MyRaceNotes="Halflings tend to be lawful good. They get a +2 to Dexterity.They are fluent and literate in Common and Halfling."
    self.MyRaceNotes=MyRaceNotes
    
    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    Dexterity=Dexterity+2
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
    self.Alignment=MyAlignment
    self.Gender=MyGender
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))

class Elf:
  def __init__(self, Name ):
    Age=random.randint(6,750)
    Height=random.randint(60,72)
    MyRaceNotes="Elves value freedom, and lean towards the gentler aspects of chaos. They get a +2 Dexterity bonus."
    self.Name = Name
    self.Size="Medium"
    self.Speed=30
    self.Height=Height
    self.Age=Age 
    self.MyRaceNotes=MyRaceNotes

    Strength=random.randint(1,20)
    Dexterity=random.randint(1,20)
    #Elves get a dex bonus of +2
    Dexterity=+2
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
    self.Alignment=MyAlignment
    self.Gender=MyGender
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))


print("\n")
print("\n")
#Name="Jane"
#Name=input("Enter a name")
choice=input("Choose a Human (H) Dwarf(D) Elf (E) or Halfling (F) to begin.")   
if choice == "H" or "h":
    character=Human(Name)
    character.introduce()
    character.stats()
elif choice=="D" or "d":
    character=Dwarf(Name)
    character.introduce()
    character.stats()
elif choice=="E" or "e":
    character=Elf(Name)
    character.introduce()
    character.stats()
elif choice=="F" or "f":
    character=Halfling(Name)
    character.introduce()
    character.stats()
else:
    print("Learn to read before you try to play DnD.")



