# Task 1: Identify The Greatest
# Write a Python program that asks the user to enter three numbers. Your code should then 
# identify and print out the largest number among the three.

number1 = input("Please give me a number in number form. ")
number2 = input("Excellent, please give me another number in number form. ")
number3 = input("Perfect, please give me one more number in number form. ")
int(number1)
int(number2)
int(number3)

if number1 > number2 and number3:
    print(number1)
elif number3 > number1 and number2:
    print(number3)
else:
    print(number2)

# Task 2: Identify The Smallest
# Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

if number1 < number2 and number3:
    print(number1)
elif number3 < number1 and number2:
    print(number3)
else:
    print(number2)