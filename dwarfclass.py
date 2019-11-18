#! python3
import random




class Dwarf:
  def __init__(self, name ):
    self.name = name
    self.Size="Medium"
    self.Speed=25
    
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
    print("Hello my name is " + self.name)
  def stats(self):
    print("Hello my name is " + self.name)

#These examples show how to print things from the dwarf class  
#Dwarf1=Dwarf("Jane")

#print("So your character "+ Dwarf1.name)
#print("Their size is "+ Dwarf1.Size)
#print("Their age is "+ str(Dwarf1.Age))
#print("Their trade Preference is: "+Dwarf1.MyTool)
#print("Here are the stats for "+Dwarf1.name+" Dwarf: ")
#print("Strength: "+ str(Dwarf1.Strength))
