# Josiah Boman
# 04/14/2020
# This program asks the user how many integers they would like to enter then prompt the user to enter
# that many integers. After the numbers have been entered, the program displays the largest and smallest
# of the numbers entered

print("How many integers would you like to enter?")
integer_count = int(input())

print("Please enter " + str(integer_count) + " integers.")

min = 100000000000
max = 0
counter = 0

while counter < integer_count:
    num_1 = int(input())
    if num_1 < min:
        min = num_1
    if num_1 > max:
        max = num_1
    counter = counter + 1
print("Min is equal to " + str(min))
print("Max is euqal to " + str(max))


