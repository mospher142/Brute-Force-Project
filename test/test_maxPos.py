import pytest
import sys
sys.path.append("../src/")


#You will need to write tests for your own functions, or change tests for ones you modify

from brute_advanced import maxPos


def test_maxPos():
    assert maxPos([1,2,3])==2
    assert maxPos([1])==0
    assert maxPos([1,-10])==0
