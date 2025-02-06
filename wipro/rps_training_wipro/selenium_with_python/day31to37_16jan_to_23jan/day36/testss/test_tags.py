import pytest

@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")

@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

@pytest.mark.sanity
def testcase3():
    print("Testcase3 is executed")

@pytest.mark.regression
def testcase4():
    print("Testcase4 is executed")