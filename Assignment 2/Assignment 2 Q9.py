#Alexander Socolovsky
#09/05/2025
#Assignment 2 Q9
Units=int(input("How much units have you used"))

if(Units<=100):
    Cents=Units*5
    print("Your total is",Cents,"cents")
elif(Units<=250):
    Units_10c=Units-100
    U_Cons_10c=Units_10c*10
    Cents=U_Cons_10c+500
    print("Your total is",Cents,"cents")
else:
    Units_20c=Units-250
    U_Cons_20c=Units_20c*20
    Cents=U_Cons_20c+2000
    print("Your total is",Cents,"cents")
