# 20. Print a triangle where each row repeats the same number.

N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(1,i+1):
        print(i,end=" ")

    print()    