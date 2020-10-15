#!/usr/bin/env python3
from brutus import Binary

#
import pathlib


# This is a starting-point for your project
# Most of the work is done for the basic task
# Intermediate will require reading from a dictionary file and creating guesses based on the contents
# For the advanced task, see the supporting module "brute_time"

#----------------------------------------------------------------------------------------------------------------------------
def create_list(list, item):
        list.append(item)
        pin = [[[(str(x) + str(y) + str(z)) for z in range(len(list))] for y in range(len(list))] for x in range(len(list))]
        return pin
    
mylist = []
for x in range(10):
    mylist = create_list(mylist, x)

def open_create_file(fl):
        file = pathlib.Path(fl)
        if file.exists ():
            with open(fl, "r") as file:
                base = file.read().split('\n')
        else:
            #create a file [list.txt] 
            with open(fl, "w+") as file:
                for y in range(len(mylist)):
                    for w in range(len(mylist[y])):
                        for z in range(len(mylist[w])):
                            file.write(f"{mylist[y][w][z]}\n")
                            
            with open(fl, "r") as file:
                base = file.read().split('\n')

        return base

file_ = open_create_file("../dictionaries/list.txt")

#----------------------------------------------------------------------------------------------------------------------------


def breakBinary(target, promptText, failText):
    """" Break into the given target binary.
    Assumes "basic" level binary, with PIN codes of 000-999
    Args:
        target: path to the binary. e.g. "./bins/basic1"
        promptText: text to look for in the output that signals a password is required. e.g. "Password:"
        failText: text that indicates an attempt failed. e.g. "Password Incorrect"
    Returns:
        None: if no successful attempt was made
        string: a successful password"""

    
    guesses=file_

    
    
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


    # Create a simple menu system to pick the binary we want to force
    targets=[]
    targets.append(["../targets/basic/basic1","Password:", "Password Incorrect"])
    targets.append(["../targets/basic/basic2","Enter the secret code:", "ACCESS DENIED"])
    targets.append(["../targets/basic/basic3","Got the PIN?", "NO"])


    print("Basic Binary Breaker")
    print("Which binary do you want to brute force?")

    for c in range(len(targets)):
        print(f"{c}: {targets[c][0]}")

    selection=int(input("Enter the number of the binary to be forced: "))

    if 0 <= selection < len(targets):
        target=targets[selection]
        breakBinary(target[0],target[1],target[2])
    else:
        print("Invalid selection")
