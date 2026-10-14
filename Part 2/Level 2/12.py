# 12. Print consecutive numbers row by row: 1 / 23 / 456/

N=int(input("enter N: "))

num=1

for i in range(1,N+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()    