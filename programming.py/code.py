n=int(input("enter the number:"))
for i in range(1,n):
    if i%2==0:
        print("_",end="")
    elif(i%2!=0):
        print("X",end="")