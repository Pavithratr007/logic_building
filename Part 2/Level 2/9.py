# 9. Print an inverted right triangle of stars.

N=int(input("enter N: "))

for i in range(N,0,-1):
    print("*" *i)