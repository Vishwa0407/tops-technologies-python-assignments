# 1. Write a Python program that takes your age as input and prints whether you are eligible to create an account on Instagram (must be 13 or older). Use if and else statements.

age = int(input("Enter your age to create an Instagram account : "))

if age >=13:
    print("Congrats ! You are now eligible to create the Instagram Account")
else:
    print("Sorry , You are not eligible to create the Instagram Account")