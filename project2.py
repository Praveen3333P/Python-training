import random

number = random.randint(1,100)
guess = int(input("Guess your number: "))
attempt = 1
while(True):
    if(guess>number and guess-number >10):
        print("The number is too big!! Give another try")
        guess = int(input("Guess another number: "))
        attempt += 1
    elif(guess>number and guess-number <10):
        print("The number is big but not that difference! you are close")
        guess = int(input("Guess another number: "))
        attempt += 1   
    elif(guess<number and number-guess >10):
        print("This number is too small!! Give another try")
        guess = int(input("Guess another number: ")) 
        attempt += 1   
    elif(guess<number and number-guess <10):
        print("This number is small but not that difference!! you are close")  
        guess = int(input("Guess another number: ")) 
        attempt += 1
    else:
        print(f"You have guessed it right in {attempt} attempts")
        break