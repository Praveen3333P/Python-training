# f = open("poems.txt","r")
# text = f.read()

# if("twinkle" in text)
#     print("It is present")
# else:
#     print("not present")
#que-2
import random
def game():
    score = random.randint(100)
    print("The score is ",score)
    return score
score  = game()    
with open("highest_score.txt","w") as f:
    highscore = int(f.read())
if score>highscore:
    with open("highest_score.txt","w") as f:
        f.write(str(score))        