# find 1^2 +2^2+3^2+....+N^

N=int(input("enter N: "))

sum=0
for i in range(1,N+1):
    sum=sum+(i*i)
print(sum)    
    
