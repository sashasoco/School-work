#Alexander Socolovsky
#24 October 2025
#Assignment 11 Q3
Total=0

Word=input("Give me a word")

for i in Word:
    
    if i.isdigit():
        i=int(i)
        Total+=i
        
print("The sum of all numbers is",Total)