# 20. Check whether a number is divisible by exactly one of 3 and 5.


n = int(input("Enter a number: "))

if (n % 3 == 0 and n % 5 != 0) or (n % 5 == 0 and n % 3 != 0):
    print("Divisible by exactly one of 3 and 5")
else:
    print("Not divisible by exactly one of 3 and 5")
