#Alexander Socolovsky
#02 September 2025
#Pg 174 Q11 (Compound interest)
Principal=int(input("Give me the amount of money you started with"))
Rate=int(input("Give me the rate of interest"))
Time=int(input("How many years have you been saving"))
Total=int(Principal*(1+Rate/100)**Time)
Compound_Int=Total-Principal
print("Your compound interest is",Compound_Int)