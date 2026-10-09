# print numbers divisible by 3 from 1 to N

n=int(input("enter n: "))
for i in range(1,n+1):
    if i%3==0:
        print(i)