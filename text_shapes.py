# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:41:19 2020

@author: MIKE Zinyoni
"""


def right_angled_triangle_triangle(n):
    '''
    *
    **
    ***
    ****
    '''
    for i in range(n):
        print('*'*i)


def rectangle(l,w):
    '''
    **********
    **********
    '''
    for i in range(w):
        print('*'*l)


def square(length):
    '''
    ***
    ***
    ***
    '''
    for i in range(length):
        print('*'*length)


def turned_right_angled_trianle(n):
    '''
        *
       **
      ***
    '''
    space = n
    for i in range(n):
        sp = " "*(space-i)
        st = '*'*i
        print(sp,st)


def equilateral_trianle(n):
    '''
        *
       ***
      *****
    '''
    space = n
    for i in range(n):
        sp = " "*(space-i)
        st = '*'*(2*i)
        print(sp,st)


def upside_down_equilateral_trianle(n):
    '''
        *
       ***
      *****
    '''
    space = n
    i=n
    while i >0:
        sp = " "*(space-i)
        st = '*'*(2*i)
        print(sp,st)
        i-=1


def rhombus(n):
    '''
      *
     ***
      *
    '''
    equilateral_trianle(n)
    upside_down_equilateral_trianle(n)


def pointed_triangles(n):
    '''
    ***
     *
    ***
    '''
    upside_down_equilateral_trianle(n)
    equilateral_trianle(n)

 
def random_plot(n):
    '''
    *******
    ***
    *****
    *******
    '''
    import random
    for i in range(n):
        print('*'*random.randint(2,15))



#print(np.random.choice(np.array(np.arange(10))))







