#Alexander Socolovsky
#02 October 2025
#Assignment 6 Q1
Amount=0
Sum=0

while True:
    Num=input("Give an integer, enter nothing to stop ")
    
    if (Num.isdigit()):
        Num=int(Num)
        Sum+=Num
        Amount+=1
        
    elif (Num.isalpha() and Num!=""):
        print("Incorrect value")
        
    elif (Num==""):
        break
Ans=Sum/Amount
print("The average is ",Ans)
        