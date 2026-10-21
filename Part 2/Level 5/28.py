# 28. Print a checkerboard pattern of stars and spaces.

N=int(input("enter N: "))

for i in range(N):
    for j in range(N):
        if (i+j)%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")

    print()            
