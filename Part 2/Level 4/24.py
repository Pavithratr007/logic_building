# 24. Print a hollow rectangle.

l=int(input("enter l: "))
b=int(input("enter b: "))

for i in range(l):
    for j in range(b):
        if i==0 or i==l-1 or j==0 or j==b-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()            
