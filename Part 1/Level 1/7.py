# 7.print the multiplication table of N

n=int(input("enter N: "))

for i in range(n,n+1):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")