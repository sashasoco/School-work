#Alexander Socolovsky
#09/08/2025
#For loop Q5
total=0
for i in range(5):
    Num=input("Give me a number")
    for Num in Num:
        Question=input("Do you want that added?").lower()
        if Question=="yes":
            Num=int(Num)
            total=total+Num
print("Your total is",total)