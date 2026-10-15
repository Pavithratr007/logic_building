# 14. Print a right-aligned triangle.

N=int(input("enter N: "))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    