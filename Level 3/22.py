# 22. Count how many even digits are present in a number.

n=int(input("enter a number: "))
count=0

while n>0:
    digit=n%10
    if digit%2==0:
      count=count+1
    n=n//10
print(count)


      