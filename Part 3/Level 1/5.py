# 5. Check whether a number is divisible by both 3 and 5.

N=int(input("enter N: "))

if N%3==0 and N%5==0:
    print("divisible by both")
else:
    print("not divisible")    