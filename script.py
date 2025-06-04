
if __name__ == '__main__':

    num1=input('Enter the first number: ')
    num2=input('Enter the second number: ')

    if num1.isdigit() & num2.isdigit():
     print(f"\nAddition: {int(num1)+int(num2)}")
     print(f"Subtraction: {int (num1) - int(num2)}")
     print(f"Multiplication: {int(num1) * int(num2)}")
     print(f"Division: {int(num1) / int(num2)}")
    else:
        print("\nInputs are not valid Numbers")

