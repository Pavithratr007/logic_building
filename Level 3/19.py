# 19.Find the product of digits of a number

n=int(input("enter digits: "))

product=1
while n>0:
    digit=n%10
    product=product*digit
    n=n//10
print(product)       

