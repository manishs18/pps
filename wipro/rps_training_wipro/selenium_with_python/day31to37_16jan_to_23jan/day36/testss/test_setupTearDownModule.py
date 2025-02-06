import pytest

def setup_module(module):
    print("API auhtorization opened")

def teardown_module(module):
    print("API authorization closed")

def testcase1():
    print("Testcase1 is executed")

def testcase2():
    print("Testcase2 is executed")
    
def testcase3():
    print("Testcase3 is executed")