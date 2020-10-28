#!/usr/bin/env python3

from brutus import Binary

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



# def averageTry(target, promptText, failText, guess, repeats=2):
#     # Provided to assist. If you use it, document it properly... :)
#     # Runs multiple attempts at cracking the binary, returning the
#     # success AND the average length of time each try took
#     results=[]
#     success=False
#     for i in range(repeats):
#         b=Binary(target)
#         b.run()
#         result=b.timedAttempt(promptText,guess, failText)
#         success=result[0]
#         results.append(result[1])
#     return (success,sum(results)/len(results))


list_ = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
item = []

insert = input("")
item = insert.split()

result = [(y+x) for y in item for x in list_]


def breakBinary(target, promptText, failText):

    #1. Use an accumulator for the current guess
    #2. in a loop, try the current guess plus each letter of the alphabest and see which one takes longest
    #3. If it is the correct password, end
    #4. If not, add the current best letter to the guess and repeat...

    guesses = result

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
