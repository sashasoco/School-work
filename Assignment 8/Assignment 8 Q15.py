#Alexander Socolovsky
#10 October 2025
#Assignment 8 Q15
list=[]

while True:
    Num=input("Give me a number, say STOP to end")
    
    if (Num=="STOP"):
        break
    
    else:
        Num=int(Num)
        list.append(Num)
       
Num_Max=max(list)

print("Your highest number is",Num_Max)
        
        
