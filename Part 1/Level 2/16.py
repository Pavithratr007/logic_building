# Find the average of N numbers entered by the user

n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    num = int(input("Enter number: "))
    sum = sum + num

average = sum / n

print("Average =", average)