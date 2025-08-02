# code by Sukant @ Cybogeek
# Write & Append to a File

file_name='output.txt'
# Take user input to write in Output File
user_input=input("Enter Text to Write to The File: ")
# Use Try block for error handling
try:
    # open the file in append mode and save the connection
    file_con=open(file_name,'a')
    # Write the file content
    content=file_con.write(user_input+'\n')
    # using new line shortcut for simplicity,
    # logic can be improved to handle multiple line entry efficiently.
    print(f'Data Successfully Written to {file_name}\n')
    # Taking another user input and append to the existing data
    input2=input('Enter Additional Text to Append: ')
    content1=file_con.write(input2+'\n')
    print('Data Successfully Appended\n')

    # Close the file Connection
    file_con.close()
    # open the file to read and save the connection
    file_con = open(file_name, 'r')
    # read the file content
    content2 = file_con.read()
    print(f'Final Content of {file_name}')
    # display the file content and close the file connection
    print(content2)
    file_con.close()


    # The finally part is a mandatory portion of Try block,
    # we can use it to display default message of continue the program flow.
finally:
    print('Writing Completed')