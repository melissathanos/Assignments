#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

given_year = int(input("Please enter a year in four digit format. Example:2023 "))

if ((given_year % 4) == 0 and (given_year % 100 != 0) or given_year % 400 == 0):
    print("That is a leap year!")
else:
    print("Try a different year.")