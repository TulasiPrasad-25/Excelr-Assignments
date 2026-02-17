# Q1) Prime numbers
# Write a Python program that checks whether a given number is prime or not. A prime number is a 
# natural number greater than 1 that has no positive divisors other than 1 and itself.
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
