import pytest
import sys
sys.path.append("../src/")
from brute_basic import create_list
import brute_basic


#You will need to write tests for your own functions, or change tests for ones you modify




def test_create_list():

    
    #This definitely needs changing and expanding
    #assert len(brute_basic.generateGuesses())==5
    assert brute_basic.create_list(list) == True

if __name__ == "__main__":
    test_create_list()