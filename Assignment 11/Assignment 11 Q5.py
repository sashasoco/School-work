#Alexander Socolovsky
#24 October 2025
#Assignment 11 Q5
Total=0

Digits=input("Give me a string of digits")

Step=int(input("Give me a step size"))

for i in Digits[::Step]:
    i=int(i)
    Total+=i

print("Your total is",Total)