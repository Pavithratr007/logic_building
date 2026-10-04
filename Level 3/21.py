# 21. Check whether a number is a palindrome.

n=int(input("enter n: "))

original=n
reverse=0

while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10   

if reverse==original:
    print("palindrome")
    
else:
    print("not a palindrome")        

