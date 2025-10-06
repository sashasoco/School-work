#Alexander Socolovsky
#02 October 2025
#Assignment 6 Q2
Grade=0
Amount=0
Sum=0

while not (Grade<0):
    Grade=int((input("Give grade, give a negative number to stop ")))
    
    if (Grade>100):
        print("Not possible")
    
    elif (Grade<0):
        break
        
    else:
        Sum+=Grade
        Amount+=1
            


Average=Sum/Amount

if Average>=90:
    Letter="A"

elif Average>=80:
    Letter="B"

elif Average>=70:
    Letter="C"

elif Average>=60:
    Letter="D"

elif Average<=59:
    Letter="F"
print("Your average grade is ",Average,"and your letter grade is",Letter) 
    

    
        
            
            
    
    