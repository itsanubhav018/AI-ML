i=0
a = "no"
b=0
while(i<=5):
    i=i+1
    
    print(f"{i}KM")
    a = input("Are you tired")

    if(a=="yes"):
         b=1
         break






if(b==1):
    print("you didn't finish the race")
else:
    print("congratulations")

