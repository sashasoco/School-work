#Alexander Socolovsky
#25/11/2025
#UTF-8 Coder
Binary="0"
Result=""
Num=""
Binary_Num=""
Count=0
Count_0_End=0
Result_No_0=""

UTF=input("Give me a UTF-8 code- U+")

for i in UTF:
      
    if i.isalpha():
        if i=="A":
            Num=10
        elif i=="B":
            Num=11
        elif i=="C":
            Num=12
        elif i=="D":
            Num=13
        elif i=="E":
            Num=14
        elif i=="F":
            Num=15
        
    else:
        Num=int(i)
    
    while (Num>0):
    
        if Num%2==0:
            Binary="0"
    
        elif Num%2==1:
            Binary="1"
        
        Num//=2
        
        Binary_Num=Binary+Binary_Num
    
    while(len(Binary_Num)<4):
        Binary_Num="0"+Binary_Num
        
    Result+=Binary_Num
    
    Binary_Num=""

for i in Result[::-1]:
   
    if i=="0":
        Count_0_End+=1
    
    else:
        break
    
print(Result)

Result_No_0=Result.strip("0")

Result_No_0+="0"*Count_0_End

if len(Result_No_0)<7:
    Result="0"+Result

elif len(Result_No_0)<10:
    Result="110"+Result[0:5]+","+"10"+Result[5:]

elif len(Result_No_0)<15:
    Result="1110"+Result[0:4]+","+"10"+Result[4:10]+","+"10"+Result[10:]

else:
    Result="1110"+Result[0:3]+","+"10"+Result[3:9]+","+"10"+Result[9:15]+","+"10"+Result[15:]


    
print(Result)
   