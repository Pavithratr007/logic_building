# 10.Find the sum of all even numbers from 1 to N

n=int(input("enter N: "))

if n%2==0:
    for i in range(1,n+1):
        if i%2==0:
            sum=n*(n+1)//2
            print(sum)
            break
              
else:
    print("odd")