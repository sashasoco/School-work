#Alexander Socolovsky
#11/09/2025
#Programming 4 Q8
Answer=1
Num=int(input("Give me a number"))

if(Num<=1):
    print("Has to be a positive number")

else:
    for i in range(Num):
        Answer*=Num
        Num-=1
print(Answer)
    
    