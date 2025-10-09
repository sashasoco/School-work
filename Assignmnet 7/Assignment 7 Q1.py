#Alexander Socolovsky
#03 October 2025
#Assignment 7 Q1
Sum=0
power=0

Num=input("Give a number ")

for i in Num:
    power+=1
    
for i in Num:
    i=int(i)
    
    Num_Cubed=i**power
    Sum+=Num_Cubed
    
Num=int(Num)
if (Num==Sum):
    print("Your number is an armstrong number")
else:
    print("Your number isnt an armstrong number")



