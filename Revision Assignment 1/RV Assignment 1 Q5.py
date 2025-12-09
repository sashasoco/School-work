#Alexander Socolovsky
#09/12/2025
#Revision Assignment 1 Q5
Sum=0

Num=int(input("Give me a number"))

for i in range(1,Num+1):
    if i%2==1:
        Sum+=i
        
print(Sum)