#Alexander Socolovsky
#03 October 2025
#Assignment 6 Q8
Num=67
Input=0
Attempt=0

while (Num!=Input):
    Input=int(input("Guess a number"))
    
    if (Input>Num):
        print("Too high")
    if (Input<Num):
        print("Too low")
    Attempt+=1

print("Well done! It took you",Attempt,"times to guess correctly")
