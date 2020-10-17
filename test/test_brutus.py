import pytest
import sys
sys.path.append("../src/")

#Here the tests are all around the "brutus" module that assists in brute-forcing
#You will need to write tests for your own functions

import brutus


def test_incorrect():
    bad_guesses=["","NO","123","aejfhskdjfhkjsdfh","-1","Swordfish", " swordfish", "swordfish "]
    for guess in bad_guesses:
        b=brutus.Binary("../test/testbin")
        b.run()    
        result=b.attempt("password:",guess,"Password Incorrect")
        assert result==False, f"'{guess}' worked as a guess, but shouldn't have"
           

def test_correct():
        b=brutus.Binary("../test/testbin")
        b.run()    
        result=b.attempt("password:","swordfish","Password Incorrect")
        assert result==True, "The correct password was used, but brutus reported it incorrect"
