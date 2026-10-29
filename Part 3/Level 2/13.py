# 13. Determine whether a triangle is equilateral, isosceles, or scalene.

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

if a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")          