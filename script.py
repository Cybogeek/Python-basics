# code by Sukant @ Cybogeek
if __name__ == '__main__':
    # input for First Number
    num1=input('Enter the first number: ')
    #input for Second Number
    num2=input('Enter the second number: ')
    # Validation for Num 1 & Num 2, make sure the input is a Number
    if num1.isdigit() & num2.isdigit():
    # Print Addition, Subtraction, Multiplication, and Divison result. Using int() for type Casting String into Integers.
     print(f"\nAddition: {int(num1)+int(num2)}")
     print(f"Subtraction: {int (num1) - int(num2)}")
     print(f"Multiplication: {int(num1) * int(num2)}")
     print(f"Division: {int(num1) / int(num2)}")
    else:
        print("\nInputs are not valid Numbers")

