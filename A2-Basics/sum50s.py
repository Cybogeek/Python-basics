# code by Sukant @ Cybogeek

# ask user for Starting Number
start=int(input("Enter Starting Number 0 or more: "))
# ask User for the Last Number in Number Series
end=int(input("Enter Last Number to Calculate: "))
# start with 0 as total sum
totalSum=0
# use for loop to iterate the Range form start to end +1, to reach desired end Number
for i in range(start,end+1):
    # add each number to the total Sum
    totalSum= totalSum + i
# Finally print formated output with the Result
print(f"The sum of Numbers from {start} to {end} is: {totalSum}")