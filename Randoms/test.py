import random

a=["Rock","Paper","Scissors"]
input1=""
while input1!="stop":
    input1=int(input("Choose 0 for Rock 1 for Paper 2 for Scissors"))
    b=random.randint(0,2)
    print(a[b])
    if input1==b:
        print("Draw")
    elif b==1:
        if input1==0:
            print("Computer wins")
        else :
            print("User wins")
    elif b==2:
        if input1==1:
            print("Computer wins")
        else:
            print("User wins")
    else :
        if input1==2:
            print("Computer wins")
        else:
            print("User wins")

    
