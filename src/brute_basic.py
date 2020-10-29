#!/usr/bin/env python3
from brutus import Binary

# as clause used to bind the name 'pro' with 'product' module from 'itertools'
# product -> https://docs.python.org/3/library/itertools.html#itertools.product
from itertools import product as pro

# use this module to work with files
import pathlib

# ----------------------------------------------------------------------------------------------------------------------------  

#function select option
def select(choise):
    return choise

#insert a value bettwen 1 and 2
value = select(int(input("1- Create a file and run\n2- Run with Itertools\nSelect your choise: ")))

if value == 1:
    # function create list
    def create_list(list, item):
    # insert inside the list itens
        list.append(item)  # -> list[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # with this for we can create a 3d array so can create a combinations like: 000-999
        pin = [[[(str(x) + str(y) + str(z)) for z in range(len(list))] for y in range(len(list))] for x in range(len(list))]
        return pin

    # create a list
    mylist = []
    for x in range(10):
        mylist = create_list(mylist, x) #insert "x" my value inside my list calling my function[create_list(list->mylist, item->"x")]

    # function to open/create a function
    def open_create_file(fl):
        file = pathlib.Path(fl)
        # if this file exists we will open this file 
        if file.exists ():
            with open(fl, "r") as file:
                base = file.read().split('\n')
        # if this file not exists we will create a new file and we will insert my list [mylist] inside a file   
        else:
            # create a file [list.txt] 
            # w+ -> write inside a file 
            with open(fl, "w+") as file:
                #this 3 for's are used to work with a 3d array
                for y in range(len(mylist)):
                    for w in range(len(mylist[y])):
                        for z in range(len(mylist[w])):
                            file.write(f"{mylist[y][w][z]}\n") # write inside the file
            
            # open and read the file                             
            with open(fl, "r") as file:
                base = file.read().split('\n')

        return base

    # add this file inside my function
    list_ = open_create_file("../dictionaries/basic/list.txt")

elif value == 2:
    
    #open and read a file
    with open("../dictionaries/basic/itertool.txt") as file:
        file_ = file.read().split('\n')
    
    create = pro(file_, repeat=3)
    list_ = [''.join(i) for i in create]
    




# ----------------------------------------------------------------------------------------------------------------------------


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

    guesses=list_

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