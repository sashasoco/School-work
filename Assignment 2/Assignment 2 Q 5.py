#Alexander Socolovsky
#09/05/2025
#Assignment 2 Q5
Rain=input("Is it raining?").lower()

if(Rain=="yes"):
    Wind=input("Is it windy?").lower()
    if "yes" in Wind:
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
    

