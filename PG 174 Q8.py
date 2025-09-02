#Alexander Socolovsky
#02 September 2025
#Pg 174 Q8
CM=float(input("Give me your height"))
Inch=float(CM*2.54)
Feet=float(Inch/12)
Inch_Rem= Feet%12
print("Your height is",Feet,"feet and",Inch_Rem,"inches")
