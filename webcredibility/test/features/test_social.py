# -*- coding: utf-8 -*-
'''
Created on Feb 5, 2012

@author: stanvp
'''
import unittest

from webcredibility.features.social import *
from webcredibility.model import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_page_rank(self):
        document = Document(url="http://google.com")
        self.assertEqual(page_rank(document), {"@page_rank": 9})

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()