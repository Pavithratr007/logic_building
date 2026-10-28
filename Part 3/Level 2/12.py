# 12. Check whether three sides can form a triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle is possible")
else:
    print("Triangle is not possible")