# Find the factorial of N

n=int(input("enter N: "))
fact=1

for i in range(1,n+1):
    fact=fact*i
print("factorial=",fact)
  