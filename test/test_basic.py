import pytest
import sys
sys.path.append("./src/")


#You will need to write tests for your own functions, or change tests for ones you modify

import brute_basic


def test_guessGenerator():
    #This definitely needs changing and expanding
    assert len(brute_basic.generateGuesses())==5
