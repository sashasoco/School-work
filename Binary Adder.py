#Alexander Socolovsky
#20 November 2025
#Binary Adder
Sum=""
Count=-1
Digit=0
Digit2=0
Carry=0

Num1=input("Give me a binary number")

Num2=input("Give me another binary number")

Length=Num1+Num2

for i in Length:
    
    if Num2[Count]=="":
        Digit2=0
    
    elif Num2[Count]=="0":
        Digit2=0
            
    elif Num2[Count]=="1":
        Digit2=1
        
    if Num1[Count]==0:
        Digit=0
        
    elif Num1[Count]==1:
        Digit=1
        
            
    if Digit+Digit2+Carry==0:
        Sum+="0"
        Carry=0
        
    elif Digit+Digit2+Carry==1:
        Sum+="1"
        Carry=0
    
    if Digit+Digit2+Carry==2:
        Carry=1
        Sum+="0"
    
    elif Digit+Digit2+Carry==3:
        Carry=1
        Sum+="1"
    
    Count-=1
    

        
    
print(Sum)   
        
    

        
    