# Q2) Product of 2 random numbers
# Develop a Python program that generates two random numbers and asks 
# the user to enter the product of these numbers. The program should 
# then check if the user's answer is correct and display an appropriate message.\
import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Ask the user for the product
user_inp = int(input(f"What is the product of {num1} and {num2}? "))
if user_inp == num1 * num2:
    print("Correct! Well done.")
else:
    print(f"Wrong answer. The correct product is {num1 * num2}.")
