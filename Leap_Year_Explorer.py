# Task 1: Leap Year Checker
# Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and 
# then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four 
# is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly 
# divisible by 400.

year = input("Please give me a year in number form. ")

if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
    print("That's a leap year! ")
else: 
    print("That's not a leap year. ")