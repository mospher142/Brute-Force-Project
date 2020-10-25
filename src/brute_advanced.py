#!/usr/bin/env python3

from brutus import Binary

# as clause used to bind the name 'pro' with 'product' module from 'itertools'
# product -> https://docs.python.org/3/library/itertools.html#itertools.product 
from itertools import chain, product

import datetime


def maxPos(seq):
    """ Given a list of numbers, return the **position** of the largest
    Args:
       seq: the list to be searched
    Returns:
       an integer position of the largest number in `seq`
    """
    maxNum=seq[0]
    maxPos=0
    for i in range(len(seq)):
        if seq[i]>maxNum:
            maxNum=seq[i]
            maxPos=i
    return maxPos

"""         
def averageTry(target, promptText, failText, guess, repeats=2):
    # Provided to assist. If you use it, document it properly... :)
    # Runs multiple attempts at cracking the binary, returning the
    # success AND the average length of time each try took
    results=[]
    success=False
    for i in range(repeats):
        b=Binary(target)
        b.run()
        result=b.timedAttempt(promptText,guess, failText)
        success=result[0]
        results.append(result[1])
    return (success,sum(results)/len(results))
"""


file = open("../dictionaries/advanced/list.txt")
read = file.read().split('\n')

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


list_ = list(bruteforce(read, 5))


def breakBinary(target, promptText, failText):

 
    guesses = list_


    for g in guesses:        

        #The actual attempt
        b=Binary(target)
        b.run()
        success=b.attempt(promptText, g, failText)

        a = datetime.datetime.now()

        if success:
            b = datetime.datetime.now()
            print(f"The Guess '{g} | {b-a}' appears to be correct")
            return g #Return the answer. No need to "break" because the return exits the function
        else:
            b = datetime.datetime.now()
            print(f"guess: {g} | {b-a} - Password incorrect!")
            

    return None #If we get here, it means we didn't return earlier in the loop with a successful guess


if __name__=="__main__":

    # Create a simple menu system to pick the binary we want to force
    targets=[]
    targets.append(["../targets/advance/advanced1","Password:", "Password Incorrect"])
    targets.append(["../targets/advance/advanced2","Password:", "Password Incorrect"])
    targets.append(["../targets/advance/advanced3","Password:", "Password Incorrect"])

    print("Intermediate Binary Breaker")
    print("Which binary do you want to brute force?")

    for c in range(len(targets)):
        print(f"{c}: {targets[c][0]}")

    selection=int(input("Enter the number of the binary to be forced: "))

    if 0 <= selection < len(targets):
        target=targets[selection]
        breakBinary(target[0],target[1],target[2])
    else:
        print("Invalid selection")
