# 7. Print a rectangle of N rows and M columns.

m=int(input("enter length: "))
n=int(input("enter breadth: "))
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()    