#Alexander Socolovsky
#14 October 2025
#Assignment 8 Q19
EvenOdd=0

N=int(input("Give me a number"))
M=int(input("give me another number to divide your first by"))

if M%2==0:
    EvenOdd=("And your second number is even")
elif M%2==1:
    EvenOdd=("And your second number is odd")

for i in range(1,N+1):
    if i%M==0:
        print(i)

print(EvenOdd)
