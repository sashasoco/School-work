#Alexander Socolovsky
#16 October 2025
#Assignment 8 Q20 B
Num=0
Total=0

N=int(input("Give me a number"))

for i in range(1,N,2):
    print(i)
    Num=i**2
    Total+=Num

Num=N**2
Total+=Num

print(Total)   
    