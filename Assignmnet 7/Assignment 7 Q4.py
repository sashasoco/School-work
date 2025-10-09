#Alexander Socolovsky
#09 October 2025
#Assignment 7 Q4

Decimal=int(input("Give me a Decimal Number"))

while (Decimal>=1):
    
    if Decimal%2==1:
        print("1")
    
    elif Decimal%2==0:
        print("0")
        
    Decimal//=2

