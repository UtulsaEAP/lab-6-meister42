def check_palindrome(user_input):
    reverse = ""
    for i in user_input: 
        reverse = i + reverse

    if reverse == user_input:
        return True
    else:
        return False
    
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
    if check_palindrome(user_input) == True:
        print("palindrome: " + str(user_input))
    else:
        print("not a palindrome: " + str(user_input))
