'''
Copyright (c) Mark Vismer 2015
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
   
import os
import sys


path = os.path.realpath(os.path.abspath(os.path.join(__file__,'../../..')))
sys.path.append(path)

import traceback

import unittest
from utils import TextTestResultPlus


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        print('Setup')
        
    def tearDown(self):
        print('Tear down'):

    def test_01(self):
        print('Test 01')
    
    
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    runner = unittest.TextTestRunner(
            resultclass= TextTestResultPlus, 
            verbosity=3)

    #suite = unittest.TestLoader().loadTestsFromTestCase(test_filter_block_comments)
    #runner.run(suite)
    unittest.main(testRunner=runner, exit=False)
    #unittest.main()
    #unittest.