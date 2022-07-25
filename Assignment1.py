
#Name: Akshatha Vasant Hegde
#Pledge: I pledge my honor that I have abided by the Stevens Honor System

from functools import reduce
import math



def mult(x,y):
    """ returns product of x and y """
    return (x * y)


def factorial(n):
    """ returns factorial of integer given """
    p = reduce(mult, range(1,n+1))
    return p




def add(x,y):
    """ returns sum of x and y """
    return (x + y)


def mean(l):
    """ returns mean of the list given """
    length = len(l);
    x = reduce(add , l);
    return x/length





