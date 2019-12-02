#! python3
import random

def roll_five_d6():
    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    roll3=random.randint(1,6)
    roll4=random.randint(1,6)
    roll5=random.randint(1,6)

    rolls=[roll1,roll2,roll3,roll4,roll5]

    sortedrolls=sorted(rolls)
    stat=sortedrolls[2]+sortedrolls[3]+sortedrolls[4]
    
    return stat

