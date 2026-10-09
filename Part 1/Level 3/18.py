# 18.Find the sum of digits of a number

n=int(input("enter number:" ))

sum=0

for i in range(1,n+1):
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)    
