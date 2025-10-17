#Alexander Socolovsky
#17 October 2025
#Strings Q3
Without=""

Word=input("Give me a word")

if (Word[0]=="a" or Word[0]=="e" or Word[0]=="i" or Word[0]=="o" or Word[0]=="u"):
    New_Word=Word+"way"

else:
    for i in range(1,len(Word)):
        Without=Without+Word[i]
        New_Word=Without+Word[0]+"ay"

print(New_Word)




    
