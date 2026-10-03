# 20.Reverse a number

n=int(input("enter digits: "))

reverse=0
while n>0:
    digit=n%10
    reverse=reverse+digit
    n=n//10
print(reverse)
