# 16. Print a centered pyramid of stars

N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(N-i):
        print(" ",end=" ")

    for k in range(2*i-1):    
        print("*",end=" ")

    print()    