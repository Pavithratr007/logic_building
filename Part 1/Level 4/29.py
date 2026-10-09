# 29. Find the GCD of two numbers.

a=int(input("enter a value: "))
b=int(input("enter b value: "))

while b!=0:
    r=a%b
    a=b
    b=r
print("GDC:",a)    





