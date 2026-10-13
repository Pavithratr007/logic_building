# 10. Print a number triangle: 1 / 12 / 123 / …

N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()