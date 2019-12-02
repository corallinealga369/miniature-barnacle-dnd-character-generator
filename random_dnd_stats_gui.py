#! python3
from tkinter import *
import random
import roll5d6
import csv

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title(" Random Stats Roller ")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        label1=Label(self,text="Enter Character Name: ")
        label1.place(x=10,y=10)
        label1.config(font=('helvetica',12))

        e1=Entry(self)
        e1.place(x=180,y=10)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        def roll_stats():
            
            Strength=roll5d6.roll_five_d6()          
            Dexterity=roll5d6.roll_five_d6()          
            Constitution=roll5d6.roll_five_d6()          
            Intelligence=roll5d6.roll_five_d6()            
            Wisdom=roll5d6.roll_five_d6()          
            Charisma=roll5d6.roll_five_d6()
            
            Name=e1.get()
            
            Race=["Dwarf","Gnome","Dragonborn", "Half-Elf","Teifling","Half-Orc","Halfling","Elf","Human"]
            Gender=["Man","Woman"]
            LifeStage=["Child", "Adult","Elderly"]
            
            
            MyGender=random.choice(Gender)
            MyRace=random.choice(Race)
            LifeStage='Adult'


            if MyRace=="Human":
                Age=random.randint(6,90)
                if Age < 18:
                    LifeStage='Child'
                elif Age > 65:
                    LifeStage='Elderly'
                else: 
                    LifeStage='Adult'
            elif MyRace=="Dwarf":
                Age=random.randint(6,350)
                if Age < 18:
                    LifeStage='Child'
                elif Age > 200:
                    LifeStage='Elderly'
                else:
                    LifeStage='Adult'
            elif MyRace=="Halfling":
                Age=random.randint(6,250)
                if Age < 20:
                    LifeStage='Child'
                elif Age > 150:
                    LifeStage='Elderly'
                else: 
                    LifeStage='Adult'
            elif MyRace=="Elf":
                Age=random.randint(6,750)
                if Age < 100:
                    LifeStage='Child'
                elif Age > 650:
                    LifeStage='Elderly'
                else: 
                    LifeStage='Adult'    
            elif MyRace=="Dragonborn":
                Age=random.randint(1,80)
                if Age < 15:
                    LifeStage='Child'
                elif Age > 65:
                    LifeStage='Elderly'
                else:
                    LifeStage='Adult'  
            elif MyRace=="Gnome":
                Age=random.randint(6,20)
                if Age < 20:
                    LifeStage='Child'
                elif Age > 200:
                    LifeStage='Elderly'
                else:
                    LifeStage='Adult' 
            elif MyRace=="Half-Elf":
                Age=random.randint(6,180)
                if Age < 20:
                    LifeStage='Child'
                elif Age > 150:
                    LifeStage='Elderly'
                else:
                     LifeStage='Adult'    
            elif MyRace=="Half-Orc":
                Age=random.randint(6,75)
                if Age < 14:
                    LifeStage='Child'
                elif Age > 60:
                    LifeStage='Elderly'
                else:
                    LifeStage='Adult'   
            elif MyRace=="Teifling":
                Age=random.randint(6,100)
                if Age < 18:
                    LifeStage='Child'
                elif Age > 70:
                    LifeStage='Elderly'
                else:
                    LifeStage='Adult'      
              
            label8=Label(self,text="                                                          " )
            label8.place(x=10, y=190) 

            label2=Label(self,text="Strength: "+str(Strength)+"  ", font=('helvetica',12))
            label2.place(x=30,y=50)

            label3=Label(self,text="Dexterity: "+str(Dexterity)+"  ", font=('helvetica',12))
            label3.place(x=30,y=70)

            label4=Label(self,text="Constitution: "+str(Constitution)+"  ", font=('helvetica',12))
            label4.place(x=30,y=90)

            label5=Label(self,text="Intelligence: "+str(Intelligence)+"  ", font=('helvetica',12))
            label5.place(x=30,y=110)

            label6=Label(self,text="Wisdom: "+str(Wisdom)+"  ", font=('helvetica',12))
            label6.place(x=30,y=130)

            label7=Label(self,text="Charisma: "+str(Charisma)+"  ", font=('helvetica',12))
            label7.place(x=30,y=150)
            
            label8=Label(self,text="So your character "+Name+" is a "+str(Age)+" year old "+LifeStage+" "+MyRace+" "+MyGender+".      " , font=('helvetica',12))
            label8.place(x=10, y=190)
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

        printButton=Button(text='Click to roll for random stats', command=roll_stats, bg='black', fg='white', font=('helvetica', 12, 'bold'))
        printButton.place(x=230, y=250)
        
    def client_exit(self):
        exit()

root = Tk()

root.geometry("500x300")

app = Window(root)
root.mainloop()  