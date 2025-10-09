#Alexander Socolovsky
#07 October 2025
#Assignment 7 Q2
Stop=0
Pos_Num=0
Neg_Num=0


while True:
    Num=float(input("Give a number, type 0 to stop"))
    
    if (Num==Stop):
        break
    
    elif (Num>0):
        Pos_Num+=1
    else
        Neg_Num+=1
print("You have input",Pos_Num,"positive numbers and",Neg_Num,"negative numbers")