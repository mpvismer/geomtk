# -*- coding: utf-8 -*-
"""
"""
import os
import sys
from testhelper import TextTestResultPlus
import unittest

if __name__ == '__main__':
    try:
        # Redirect err to stdout to sync test decoration
        # save stderr for logging
        old = sys.stderr
        sys.stderr = sys.stdout
        runner = unittest.TextTestRunner(
            resultclass=TextTestResultPlus,
            stream=sys.stdout,  # All test decoration to stdout to prevent mixing
            verbosity=3)
        tests = unittest.defaultTestLoader.discover(
            os.path.join(__file__, '..'))
        print("Discovered {} tests.\n".format(tests.countTestCases()))
        runner.run(tests)
    finally:
        sys.stderr = old
