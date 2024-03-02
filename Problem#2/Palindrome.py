"""
Name: Henry Holman
Lab time: Thursday 2 pm


"""


def check_palindrome(user_input):
    reverse = ""
    for i in user_input: 
        reverse = i + reverse

    if reverse == user_input:
        print("palindrome: " + str(user_input))
    else:
        print("not a palindrome: " + str(user_input))
    
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
