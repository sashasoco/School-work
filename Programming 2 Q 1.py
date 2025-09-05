#Alexander Socolovsky
#09/05/2025
#Assignment 2 Q1
Num1=int(input("Give me a number"))
Num2=int(input("Give me another number"))
if(Num1==Num2):
    print("Your numbers must be different")
elif(Num2<Num1):
    print("Your first number is bigger than the second")
elif(Num1<Num2):
    print("Your second number is bigger than the first")