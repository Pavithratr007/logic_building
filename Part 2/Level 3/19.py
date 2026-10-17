# 19. Print a centered palindrome number pyramid: 1 / 121 / 12321
 
N=int(input("enter N: "))

for i in range(1,N+1):
    for j in range(N-i):
        print(" ",end=" ")

    for k in range(1,i+1):    
        print(k,end=" ")

    for k in range(i-1,0,-1):
        print(k,end=" ")    
        

    print()   