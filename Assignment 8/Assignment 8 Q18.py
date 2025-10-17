#Alexander Socolovsky
#10 October 2025
#Assignment 8 Q18
Digits=0

X=input("Give me a number")

for i in X:
    Digits+=1
    
Signif=X[0]

Digits*=10
Signif=int(Signif)

Y=Digits+Signif
print(Y)







