# # 17.Count the number of digits in a number

n=int(input("enter digits: "))

count=0
for i in range(len(str(n))):
    count=count+1
print("numbers of digits:",count)    