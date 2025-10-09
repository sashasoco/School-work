#Alexander Socolovsky
#07 October 2025
#Assignment 7 Q3
Power=-1
Power2=0
Decimal=0
i_Pow=0

Binary=input("Give me a binary number")

for i in Binary:
    Power+=1
    

for i in Binary:
    i=int(i)
    
    Power2=2**Power
    i_Pow=i*Power2
    Decimal+=i_Pow
    
    Power-=1
    
print(Decimal)
    