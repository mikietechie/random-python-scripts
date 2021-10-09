# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:17:35 2020

@author: MIKE
"""

def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * factorial(n-1)
