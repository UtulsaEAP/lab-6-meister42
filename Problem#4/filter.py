"""
Name: Henry Holman
Lab time: Thursday 2 pm
"""

def process_and_print(input_string):
    # Split into separate strings
    input_data = input_string.split(" ")

    # Convert strings to integers and filter out negative values
    inted = []
    for i in input_data:
        inted.append(int(i))
    allnegatives = []
    for i in inted:
        if i < 0:
            allnegatives.append(i)
    
    # Sort integers in reverse order
    ordered = sorted(allnegatives)
    ordered.reverse()

    # Print sorted integers
    printstring = ""
    for i in ordered:
        printstring += (str(i) + " ")
    print(printstring, end = "")

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
