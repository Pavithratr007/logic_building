# 27. check whether a number is prime.

n = int(input("Enter a number: "))

if n <= 1:
    print("Not prime")
else:
    count = 0

    for i in range(2, n):
        if n % i == 0:
            count += 1

    if count == 0:
        print("Prime number")
    else:
        print("Not prime")