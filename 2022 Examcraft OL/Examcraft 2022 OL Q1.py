#Alexander Socolovsky
#03/13/2025
#Examcraft 2022 OL Q1

print("This program can fine the area or perimiter of a quadilateral")

length=float(input("Please enter the length"))
width=float(input("Please enter the width"))

name=input("What is your name?")

choice=input("Do you want to find the (p)erimiter or (a)rea?")

if choice=="p":
    result=(length*2)+(width*2)
    aorp="perimeter"
elif choice=="a":
    result=(length*width)
    aorp="area"

result=round(result,2)
print("A quadrilateral with a length of",length,"and a width of",width,"has an",aorp,"of",result)

print("Thank you for using this program",name)
