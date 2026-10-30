# 15. Build a simple calculator using +, −, ×, and ÷.

# 1. Take inputs
num1 = float(input("Enter first number: "))
optr = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# 2. Process logic using match-case or if-else
if optr == '+':
    result = num1 + num2
elif optr == '-':
    result = num1 - num2
elif optr == '*':
    result = num1 * num2
elif optr == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# 3. Output result
print("Result:", result)




            
