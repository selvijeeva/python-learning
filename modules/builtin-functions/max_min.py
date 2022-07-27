# Read three numbers, using max and min function find the largest and smallest number

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)

smallest_number = min(number1,number2,number3)
print("The smallest number is:", smallest_number)