# 13. Print a decreasing-number triangle: 5 / 54 / 543/...

N=int(input("enter N: "))


for i in range(1,N+1):
    for j in range(N,N-i,-1):
        print(j,end=" ")
    print()    