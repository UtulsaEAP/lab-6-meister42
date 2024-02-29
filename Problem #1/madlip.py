"""
Name: Henry Holman
Lab Time: Thursday 2 pm

"""

def food_input():
    user_input = input()
    tokens = user_input.split(" ")
    tokendictionary = {}
    while tokens[0] != "quit":
        tokendictionary[tokens[0]] = tokens[1]
        user_input = input()
        tokens = user_input.split(" ")
    
    for i in tokendictionary:
        print("Eating %s %s a day keeps you happy and healthy." % (tokendictionary[i], i))
    

if __name__ == "__main__":
    food_input()
