# 27. Print a dynamic hollow square for any N.

N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==1 or i==N or j==1 or j==N:
            print("*",end=" ")
        else:
            print(" ",end=" ")  

    print()          