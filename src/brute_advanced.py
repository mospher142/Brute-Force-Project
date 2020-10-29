#!/usr/bin/env python3

from brutus import Binary
import sys



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


def averageTry(target, promptText, failText, guess, repeats=2):
#     # Provided to assist. If you use it, document it properly... :)
#     # Runs multiple attempts at cracking the binary, returning the
#     # success AND the average length of time each try took
    results=[]
    success=False
    for i in range(repeats):
        b=Binary(target)
        b.run()
        result=b.timedAttempt(promptText,guess, failText)
        success=result[0]
        results.append(result[1])
    return (success,sum(results)/len(results))



def breakBinary(target, promptText, failText):

    list_ = [] #this list contains the alphabet
    letter = "a" #the first letter
    delay = 0 
    delay_ = False
    maximun = 0
    index = ""
    password = [""]
    
    #Create a list since a-z
    for y in range(0, 26):
        list_.append(letter)
        letter = chr(ord(letter) + 1)

    #delay[0] -> True or False
    #delay[1] -> Time
    while delay_ != True:
        for y in list_:
            for x in password:
                delay = averageTry(target, promptText, failText, x+y)
                delay_ = delay[0] # = FALSE
                print(f"{x+y} | {delay_}")
                if delay[1] > maximun: 
                    maximun = delay[1]
                    index = y
                    delay_ = delay[0] 
                if delay_ == True:
                    sys.exit() #exit the program
        
        print('\033c') # clean console
        password[0] += index   
        maximun = 0
        index = 0 
        print(*password)
       
        

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
