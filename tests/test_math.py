import os
import sys
import pytest

PROJECT_PATH = os.getcwd()
sys.path.append(PROJECT_PATH)

from example.math import add

def test_add():
    assert add(1,2) == 3 

def test_add_negative():
    assert add(1,-2) == -1