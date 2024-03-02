"""
Name: Henry Holman
Lab time: Thursday 2 pm
"""

def filter_and_print_range(integer_list, min_val, max_val):
    #write your code here
    outputstring = ""
    for i in integer_list:
        if i in range(int(min_val), int(max_val) + 1):
            outputstring = outputstring + str(i) + ","
    print(outputstring, end = "")


if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = []
    for i in user_input.split(" "):
        integer_list.append(int(i))

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = user_input.split(" ")
    filter_and_print_range(integer_list, min_val, max_val)

    # Call the function to filter and print the numbers in the given range
   
