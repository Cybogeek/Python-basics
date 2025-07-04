# code by Sukant @ Cybogeek
# define function to find factorial, It takes a number as argument
def factorial(number):
    if number<2:
        # use if check to return 1 for any value below 2
        return 1
    else:
        # else we will multiply the number with the factorial of its predecessor number (-1)
        return number * factorial(number - 1)

# take input from user and make sure it is an integer
num=int(input("Enter a Number: "))

# store the factorial in a result variable
result= factorial(num)
# Display the Result in proper format
print(f"Factorial of {num} is {result}")