import glob
import unittest
import os

def create_test_suite():
    prefix = "."+os.sep+"08-Milestone Project - 2"+os.sep+"cardgames"+os.sep+"test"+os.sep
    test_file_strings = glob.glob(prefix+"test_*.py")
    #print(f"test file strings = {test_file_strings}")

    module_strings = ['test.'+str[len(prefix):len(str)-3] for str in test_file_strings]
    #print(f"module strings = {module_strings}")

    suites = [unittest.defaultTestLoader.loadTestsFromName(name) for name in module_strings]
    #print(f"suites = {suites}")

    testSuite = unittest.TestSuite(suites)
    return testSuite