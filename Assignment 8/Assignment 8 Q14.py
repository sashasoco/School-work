#Alexander Socolovsky
#09 October 2025
#Assignment 8 Q14

N=int(input("Give me a number over 20"))

for i in range(11,N+1):
    if i%3==0 and i%7==0:
        print("TipsyTopsy")
    
    elif i%3==0:
        print("Tipsy")
        
    elif i%7==0:
        print("Topsy")
    
    else:
        continue