#Alexander Socolovsky
#09/09/2025
#Programming 4 Q7
Num=1

Even_Num=0
Odd_Num=0
while (Num!=int):
    Num=(input("Give me a number"))
    
    if Num%2==0:
        Even_Num+=1
    elif Num%2==1:
            Odd_Num=+1
    else:
        Num=str(Num)
    if("q"==Num):
        print(Odd_Num,Even_Num)
        
