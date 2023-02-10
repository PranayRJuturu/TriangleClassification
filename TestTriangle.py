# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 should be scalene')
        
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2,2,1),'Isosceles','2,2,1 should be isosceles')

    def testInvalidInputs(self): 
        self.assertEqual(classifyTriangle(0,300,2),'InvalidInput')

    def testInvalidInputsA(self):
        self.assertEqual(classifyTriangle(-1,20,1),'InvalidInput')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 should be scalene')


    def testEquilateralTrianglesA(self):
        self.asserEqual(classifyTriangle(1,1,2),'Equilateral','1,1,2 should be isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()