#Alexander Socolovsky
#17 October 2025
#Strings Q4
Count=0

Word=input("Give me a word:").lower()
Letter=input("Give me a letter in that word:").lower()

for i in Word:
    if i==Letter:
        Count+=1
print("The letter you chose shows up",Count,"times")