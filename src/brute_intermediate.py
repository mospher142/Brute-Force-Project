#!/usr/bin/env python3

from brutus import Binary

#MYCODE---------------------------------------------------------
def wordsFromFile(filePath):

    with open(filePath) as file:
        # convert file into a list and remove '\n'
        base = file.read().split('\n')

    return base
#----------------------------------------------------------

def breakBinary(target, promptText, failText, guesses):
    """" Break into the given target binary.
    Assumes "intermeduate level binary, with dictionary words
    Args:
        target: path to the binary. e.g. "./bins/basic1"
        promptText: text to look for in the output that signals a password is required. e.g. "Password:"
        failText: text that indicates an attempt failed. e.g. "Password Incorrect"
        guesses: list of words to try as passwords
    Returns:
        None: if no successful attempt was made
        string: a successful password""" 
    
    for g in guesses:        

        #The actual attempt
        b=Binary(target)
        b.run()
        success=b.attempt(promptText,g, failText)

        
        if success:
            print(f"The Guess '{g}' appears to be correct")
            return g #Return the answer. No need to "break" because the return exits the function
        else:
            print(f"guess: {g} - Password incorrect!")
    return None #If we get here, it means we didn't return earlier in the loop with a successful guess

    
if __name__=="__main__":

    #Load the dictionary
    document=wordsFromFile("../dictionaries/intermediate/base.txt")

    #give a password the document values
    password_digits = document

    #create a dicionary
    dicionary = {'o': '0', 'i': '1', 'e': '3', 'a': '4', 's':'5'}

    #dicionary = {'key':'value'}
    #key -> letter 
    #value -> Number
    #this will convert the letters of the word by the respective number that is in the dictionary
    for key,value in dicionary.items():
        password_digits = ([item.replace(key, value) for item in password_digits])
    
    #create a list 
    password_single_digit = []

    #create a range of 10 and past were values in a file document like:  abroad0, abroad1, abroad2,  ect... 
    for y in range(10):# range of 10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in document:
            password_single_digit.append(str(x) + str(y))#this is to append the number to the word inside the file/document

    
    #reason why i did this and didn't add new words to the list. Because then the dictionary can change and so these added passwords are useless
    word_list = (document + password_digits + password_single_digit)

    
    # Create a simple menu system to pick the binary we want to force
    targets=[]
    targets.append(["../targets/intermediate/intermediate1","Password: ", "Password Incorrect"])
    targets.append(["../targets/intermediate/intermediate2","Secret code: ", "Auth Failure"])
    targets.append(["../targets/intermediate/intermediate3","Enter Credentials: ", "Invalid Credentials"])

    print("Intermediate Binary Breaker")
    print("Which binary do you want to brute force?")

    for c in range(len(targets)):
        print(f"{c}: {targets[c][0]}")

    selection=int(input("Enter the number of the binary to be forced: "))

    if 0 <= selection < len(targets):
        target=targets[selection]                  #insert the lists
        breakBinary(target[0],target[1],target[2], word_list)
    else:   
        print("Invalid selection")
