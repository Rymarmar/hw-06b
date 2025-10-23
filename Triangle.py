# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Benedict Martinez
Pledge: I pledge my honor that I have abided by the Stevens Honor System
"""

def classifyTriangle(a,b,c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # 1. Type check first
    if not (isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # 2. Range / Sign
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # 3. Triangle Inequality (Strict)
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    # 4. Classification
    if a == b == c:
        return 'Equilateral'

    x, y, z = sorted((a, b, c))
    if x*x + y*y == z*z:
        return 'Right'

    if a == b or b == c or a == c:
        return 'Isosceles'

    return 'Scalene'