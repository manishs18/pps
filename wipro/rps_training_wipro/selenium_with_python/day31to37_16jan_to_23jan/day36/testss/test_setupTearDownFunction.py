import pytest

def setup_function(function):
    print("Opening the db connection")

def teardown_function(function):
    print("Closing the db connection")

def testcase1():
    print("Testcase1 is executed")

def testcase2():
    print("Tetscase2 is executed")
    
def testcase3():
    print("Tetscase3 is executed")