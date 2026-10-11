# 6. Print an N × N square of stars.

N=int(input("enter N: "))
for i in range(N):
    for j in range(N):
        print("*",end=" ") 
    print()

        