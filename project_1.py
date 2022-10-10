import random
def rock_papaer_scissors(computer,mine):
    print(f"you chose {mine} and the computer chose {computer}")  
    if(mine=="rock" and computer=="scissors"):
        return True
    elif(mine=="paper" and computer=="rock"):
        return True
    elif(mine=="scissors" and computer=="paper"):
        return True
    else:    
        return False 
                   
choice = ('rock','paper','scissors')
computer = random.randint(0,2)
computer = choice[computer]
mine = input("Choose either Rock,Paper or Scissors: ")

win = rock_papaer_scissors(computer,mine)
if win:
    print("You won")
elif(mine==computer):
    print("Draw match")
else:
    print("you lost")    