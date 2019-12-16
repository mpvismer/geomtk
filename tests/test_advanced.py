# -*- coding: utf-8 -*-

from .context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
    
    @classmethod
    def setUpClass(cls):
        print("Called at each fixture setup.")
    
    @classmethod
    def tearDownClass(cls):
        print("Called at each fixture setup.")
    
    def setUp(self):
        print("Called BEFORE each test case.")

    def tearDown(self):
        print("Called AFTER each test case.")

    def test_thoughts(self):
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()
