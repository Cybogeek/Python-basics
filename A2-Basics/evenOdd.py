# code by Sukant @ Cybogeek

#use int function to make sure input is integer
num=int(input("Enter a Number: "))
# checking if modulus of number by 2 is 0 or not
if num%2==0 :
    # if it's 0 then number is Even
    print(f"{num} is an Even Number")
else:
    # else the number is odd
    print(f"{num} is an odd Number")
