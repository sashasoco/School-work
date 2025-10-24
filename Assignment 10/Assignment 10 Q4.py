#Alexander Socolovsky
#23 October 2025
#Assignment 10 Q4
Count=-1
WordSliced=""

Word=input("Give me a word")

for i in Word:
    Count+=1
    
    if (Count%2==0):
        WordSliced+=i

print(WordSliced)