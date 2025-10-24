#Alexander Socolovsky
#24 October 2025
#Assignment 11 Q4
Win=67
Guess=0
Winner="False"

while Guess<7:
    
    Num=int(input("Give me a number between 1 and 100"))
    
    if Num==Win:
        Winner="True"
        break
    
    elif Num<Win:
        print("Number too small, try again")
        Guess+=1
    
    elif Num>Win:
        print("Number too big, try again")
        Guess+=1
    
if Winner=="True":
    print("You win!")

else:
    print("Game over")