#Alexander Socolovsky
#03 November 2025
#Assignment 12 Q10
Count=0
Roman_Num=""

Num=(input("Give me a digit to turn to Roman Numerals"))

for Digit in Num[::-1]:
    Digit=int(Digit)
    
    
    if Digit<4:
        
        while Digit>0:
            Roman_Num+="I"
            Digit-=1
            
    elif Digit==4:
        Roman_Num+="IV"
    
    elif Digit==9:
        Roman_Num+="IX"
    
    else:
        Roman_Num+="V"
        Digit-=5
        Roman_Num+="I"*Digit

print(Roman_Num)
            
    




    