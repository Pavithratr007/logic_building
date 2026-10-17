# 18. Print a number pyramid: 1 / 123 / 12345 / …
  

N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(N-i):
        print(" ",end=" ")

    for k in range(1,2*i):    
        print(k,end=" ")

    print()            
