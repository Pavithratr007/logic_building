# 11. Print a repeated-number triangle: 1 / 22 / 333 / …

N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()    