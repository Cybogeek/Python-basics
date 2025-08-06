# code by Sukant @ Cybogeek
# Example with dictionary

dict_students={'John':45,'Pam':52,'Angela':48,'Tiger':51,'Gordon':55}

print('Available Students in Record')
for i in dict_students:
    print(i)

student=input("Enter Student's name: ")

if student in dict_students:
    print(f"{student}'s marks: {dict_students[student]}")
else:
    print(f' No Record found for {student}')