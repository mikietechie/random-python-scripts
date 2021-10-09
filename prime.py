# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:24:11 2020

@author: MIKE
"""

def is_prime(n):
    prime = True
    for i in range(2,n):
        if (n%i == 0):
            prime = False
            break
    return prime
