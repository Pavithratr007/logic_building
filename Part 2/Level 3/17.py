# 17. Print an inverted centered pyramid.

N=int(input('enter N: '))

for i in range(N):
    for j in range(i):
        print(" ",end=" ")

    for k in range(2*(N-i)-1):
        print("*",end=" ") 

    print()  