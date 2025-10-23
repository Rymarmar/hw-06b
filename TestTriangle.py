# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Valid Triangles:

    def test_equilateral_basic(self):
        # sanity: all sides equal -> Equilateral
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral")

    def test_isosceles_permutations(self):
        # two equal sides, try every position, just to be safe
        for sides in [(3,3,4), (3,4,3), (4,3,3)]:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "Isosceles")

    def test_scalene_non_right(self):
        # no equal sides and not a Pythagorean triple
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene")

    def test_right_3_4_5_all_perms(self):
        # classic triple, check all permutations 
        perms = [(3,4,5),(3,5,4),(4,3,5),(4,5,3),(5,3,4),(5,4,3)]
        for sides in perms:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "Right")

    def test_right_5_12_13_all_perms(self):
        perms = [(5,12,13),(5,13,12),(12,5,13),(12,13,5),(13,5,12),(13,12,5)]
        for sides in perms:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "Right")

    # Not a triangle (triangle inequality):

    def test_triangle_inequality_fails(self):
        # sum of two sides must be greater than third
        for sides in [(1,1,3),(2,3,5),(10,1,1)]:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "NotATriangle")

    # Invalid inputs:

    def test_zero_or_negative(self):
        # non-positive values are invalid
        for sides in [(0,5,5),(5,0,5),(5,5,0),(-1,2,2)]:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "InvalidInput")

    def test_non_integer_types(self):
        # the starter expects ints, float/str should be invalid
        for sides in [(3.5,3,3),("3",3,3)]:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "InvalidInput")

    def test_out_of_range_high(self):
        # per starter, anything greater than 200 is invalid
        for sides in [(201,199,199),(1000,1,1)]:
            with self.subTest(sides=sides):
                self.assertEqual(classifyTriangle(*sides), "InvalidInput")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
