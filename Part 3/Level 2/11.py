# 11. Find the smallest of three numbers.

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

small =a

if b<a:
    print("b is small")
elif c<a:
    print("c is small")
elif a==b==c: 
    print("all are equal") 
else:
    print("a is samll")            