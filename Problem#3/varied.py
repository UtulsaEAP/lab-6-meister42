"""
Name: Henry Holman
Lab time: Thursday 2 pm
"""

import statistics
def process_input(input_string):
    # Split into separate strings
    stringed = input_string.split(" ")
    
    # Convert strings to floats
    floated = []
    for i in range(0, len(stringed)):
      floated.append(float(stringed[i]))
    
    # Get max and average
    max_value = max(floated)
    average_value = statistics.mean(floated)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    #print(f'Max Value: {max_value:.2f}')
    #print(f'Average Value: {average_value:.2f}')

    print(f'{max_value} {average_value}')
