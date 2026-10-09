# 12.Find the sum of numbers divisible by 3 from 1 to N

n=int(input("enter N: "))

if n%3==0:
    for i in range(1,n+1):
        if i%3==0:
            sum=n*(n+1)//2
            print(sum)
            break

else:
    print("N is not divisible by 3")        