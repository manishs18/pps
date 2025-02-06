import pytest


def testcase1():
    print("Testcase1 is executed")

@pytest.mark.skip
def testcase2():
    print("Testcase2 is executed")

@pytest.mark.xfail
def testcase3():
    print("Testcase3 is executed")

def testcase4():
    print("Testcase4 is executed")