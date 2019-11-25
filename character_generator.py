#! python3
import random
import time
import csv

Name="Jane Doe"
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
Race=["Dwarf","Halfling","Elf","Human"]
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
    self.dict={

    Name:self.Name,
    Size:self.Size,
    Speed:self.Speed,
    Height:self.Height,
    Age:self.Age,
    Strength:self.Strength,
    Dexterity:self.Dexterity,
    Constitution:self.Constitution,
    Intelligence:self.Intelligence,
    Wisdom:self.Wisdom,
    Charisma:self.Charisma,
    Alignment:self.Alignment,
    Gender:self.Gender,

    }
    
  def introduce(self):
    print("Hello my name is " + self.Name)

  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))

  def print_dict(self):
    #This will print all the values for the character that are included in the dictionary
    time.sleep(2)
    print("Here are the stats and notes for your character")
    print("\n")
    for key, value in character.dict.items():
        print(f"{key}:{value}")
    print("\n")
    
class Human:
  def __init__(self, name ):
    self.Name = Name
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
    self.dict={

        0:self.Name,
        1:self.Size,
        2:self.Speed,
        3:self.Height,
        4:self.Age,
        5:self.Strength,
        6:self.Dexterity,
        7:self.Constitution,
        8:self.Intelligence,
        9:self.Wisdom,
        10:self.Charisma,
        11:self.Alignment,
        12:self.Gender,

    }
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))
  def print_dict(self):
    #This will print all the values for the character that are included in the dictionary
    time.sleep(2)
    print("Here are the stats and notes for your character")
    print("\n")
    for key, value in character.dict.items():
        print(f"{key}:{value}")
    print("\n")
    
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
    self.dict={

    Name:self.Name,
    Size:self.Size,
    Speed:self.Speed,
    Height:self.Height,
    Age:self.Age,
    Strength:self.Strength,
    Dexterity:self.Dexterity,
    Constitution:self.Constitution,
    Intelligence:self.Intelligence,
    Wisdom:self.Wisdom,
    Charisma:self.Charisma,
    Alignment:self.Alignment,
    Gender:self.Gender,

    }
    
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))
  def print_dict(self):
    #This will print all the values for the character that are included in the dictionary
    time.sleep(2)
    print("Here are the stats and notes for your character")
    print("\n")
    for key, value in character.dict.items():
        print(f"{key}:{value}")
    print("\n")

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
    self.dict={

    Name:self.Name,
    Size:self.Size,
    Speed:self.Speed,
    Height:self.Height,
    Age:self.Age,
    Strength:self.Strength,
    Dexterity:self.Dexterity,
    Constitution:self.Constitution,
    Intelligence:self.Intelligence,
    Wisdom:self.Wisdom,
    Charisma:self.Charisma,
    Alignment:self.Alignment,
    Gender:self.Gender,

    }
  def introduce(self):
    print("Hello my name is " + self.Name)
  def stats(self):
    print("Strength:"+str(self.Strength))
    print("Dexterity:"+str(self.Dexterity))
    print("Consitution:"+str(self.Constitution))
    print("Intelligence:"+str(self.Intelligence))
    print("Wisdom:"+str(self.Wisdom))
    print("Charisma:"+str(self.Charisma))
  def print_dict(self):
    #This will print all the values for the character that are included in the dictionary
    time.sleep(2)
    print("Here are the stats and notes for your character")
    print("\n")
    for key, value in character.dict.items():
        print(f"{key}:{value}")
    print("\n")

choice=input("Choose a Human (H) Dwarf(D) Elf (E) or Halfling (F) to begin.")   
if choice == "H" or "h":
    character=Human(Name)
    character.introduce()
    time.sleep(2)
    character.stats()
    time.sleep(2)
    character.print_dict()

elif choice=="D" or "d":
    character=Dwarf(Name)
    character.introduce()
    time.sleep(2)
    character.stats()
    time.sleep(2)
    character.print_dict()
    
elif choice=="E" or "e":
    character=Elf(Name)
    character.introduce()
    time.sleep(2)
    character.stats()
    time.sleep(2)
    character.print_dict()

elif choice=="F" or "f":
    character=Halfling(Name)
    character.introduce()
    time.sleep(2)
    character.stats()
    time.sleep(2)
    character.print_dict()
else:
    print("Learn to read before you try to play DnD.")

#this is not currently used in the script
def make_text_file(character):
#this creates a raw text file.
  f = open("mycharacter.txt","w")
  f.write( str(character.dict.items()) )
  f.close()

def make_csv_file(character):
#This creates a comma seperated value file
  w = csv.writer(open( "mycharacter.csv", "w"))
  for key, val in character.dict.items():
      w.writerow([key, val])
  print("You now have a text file and csv with your character stats!")
  print("You can open the csv in Excel or Google Docs.")
  w.close()

filechoice=input("Would you like to print a CSV of your character to save? Enter 1 for yes, or any other key for no. ")
if filechoice==1:
  make_csv_file(character)
  print("Thanks for saving your character! See you again later!")
else: 
  print("Thanks for using the character generator! Bye!")
