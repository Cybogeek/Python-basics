# code by Sukant @ Cybogeek
# Read a File and handle errors

file_name='sample.txt'
# Use Try block for error handling
try:
    # open the file and save the connection
    file_con=open(file_name,'r')
    # read the file content in an array
    content=file_con.readlines()
    print('Reading File Content')
    # spread the array to display each Line with custom formating
    for i in content:
        print(f' Line {content.index(i)}: {i}')

    # Close the file Connection
    file_con.close()
    # expect the File Not Found Error and display custom Message accordingly
except FileNotFoundError:
    print(f"Error: The File {file_name} was not Found. ")

    # The finally part is a mandatory portion of Try block,
    # we can use it to display default message of continue the program flow.
finally:
    print('Line Reading Completed')