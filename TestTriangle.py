# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInputType(self):
        self.assertEqual(classify_triangle('a', 2, 2), "InvalidInput")
        self.assertEqual(classify_triangle(2, 'b', 2), "InvalidInput")
        self.assertEqual(classify_triangle(2, 2, 'c'), "InvalidInput")

    def testInputValueBoundary(self):
        self.assertEqual(classify_triangle(-1, 2, 2), "InvalidInput")
        self.assertEqual(classify_triangle(2, -1, 2), "InvalidInput")
        self.assertEqual(classify_triangle(2, 2, -1), "InvalidInput")
        self.assertEqual(classify_triangle(201, 150, 150), "InvalidInput")
        self.assertEqual(classify_triangle(150, 201, 150), "InvalidInput")
        self.assertEqual(classify_triangle(150, 150, 201), "InvalidInput")

    def testInputValueDecimal(self):
        self.assertEqual(classify_triangle(2.1, 2, 2), "InvalidInput")
        self.assertEqual(classify_triangle(2, 2.1, 2), "InvalidInput")
        self.assertEqual(classify_triangle(2, 2, 2.1), "InvalidInput")

    def testNotATriangle01(self):
        self.assertEqual(classify_triangle(5, 1, 2), "NotATriangle")

    def testNotATriangle02(self):
        self.assertEqual(classify_triangle(5, 2, 3), "NotATriangle")

    def testNotATriangle03(self):
        self.assertEqual(classify_triangle(1, 2, 5), "NotATriangle")

    def testNotATriangle04(self):
        self.assertEqual(classify_triangle(2, 3, 5), "NotATriangle")

    def testNotATriangle05(self):
        self.assertEqual(classify_triangle(1, 5, 2), "NotATriangle")

    def testNotATriangle06(self):
        self.assertEqual(classify_triangle(3, 5, 2), "NotATriangle")

    def testIsoscelesTriangle01(self):
        self.assertEqual(classify_triangle(3, 3, 2), "Isosceles")

    def testIsoscelesTriangle02(self):
        self.assertEqual(classify_triangle(2, 3, 3), "Isosceles")

    def testIsoscelesTriangle03(self):
        self.assertEqual(classify_triangle(3, 2, 3), "Isosceles")

    def testRightTriangle01(self):
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangle02(self):
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangle03(self):
        self.assertEqual(classify_triangle(3,5,4),'Right','3,5,4 is a Right triangle')

    def testScaleneTriangle01(self):
        self.assertEqual(classify_triangle(6, 3, 4), 'Scalene')

    def testScaleneTriangle02(self):
        self.assertEqual(classify_triangle(3, 6, 4), 'Scalene')

    def testScaleneTriangle03(self):
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

