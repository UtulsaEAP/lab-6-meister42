def process_user_contacts(user_input):
    user_contacts = user_input.split(" ")
    tokens = {}
    for i in range(0, len(user_contacts)):
        entry = (user_contacts[i]).split(",")
        tokens[entry[0]] = entry[1]
    # Put word pairs into a dict
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(tokens[contact_name])
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
