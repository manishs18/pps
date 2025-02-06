import pytest

class TestClass:

    def setup_class(cls):
        print('Opening the db connection')

    def teardown_class(cls):
        print('Closing the db connection')

    def setup_method(self, method):
        print('Open browser')

    def teardown_method(self, method):
        print('Close browser')

    def testcase1(self):
        print('Testcase1 is executed')

    def testcase2(self):
        print('Testcase2 is executed')

    def testcase3(self):
        print('Testcase3 is executed')
