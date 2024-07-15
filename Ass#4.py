'''Assignment_4
#Q: Write a Python program that take input from the user and calculates the factorial of a given positive integer using a for loop. The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 5!=5×4×3×2×1=120.'''


number= int(input("Enter a Number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i
    
print("Factorial: ",factorial)