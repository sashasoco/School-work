#Alexander Socolovsky
#03/13/2025
#Examcraft 2022 OL Q2
import random

com_opt=["rock","paper","scissors"]

com_choice=com_opt[random.randint(0,2)]

player_choice=input("Choose rock, paper or scissors")

print("You chose",player_choice)
print("Computer chose",com_choice)

if com_choice==player_choice:
    print("Draw!")

elif com_choice=="rock":
    if player_choice=="paper":
        print("You win!")
    else:
        print("You lose!")

elif com_choice=="paper":
    if player_choice=="scissors":
        print("You win!")
    else:
        print("You lose!")

elif com_choice=="scissors":
    if player_choice=="rock":
        print("You win!")
    else:
        print("You lose!")

        

