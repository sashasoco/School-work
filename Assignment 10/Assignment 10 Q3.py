#Alexander Socolovsky
#23 October 2025
#Assignment 10 Q3

Word=input("Give me a word")

Letter=Word[0]
Replace="$"

WordWo1=Word[1:]

Word=WordWo1.replace(Letter,Replace)

Word=Letter+Word

print(Word)
