# 10. Find the greatest of three numbers.

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

a=0

if a>=b or a>=c:
    print("a is large")
elif b>=c:
    print("b is large")
else:
    print("c is large")      


