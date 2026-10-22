# 29. Print a 0–1 triangle, alternating 0 and 1.

N=int(input("enter N: "))

for i in range(1,N-1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")       
    print()        