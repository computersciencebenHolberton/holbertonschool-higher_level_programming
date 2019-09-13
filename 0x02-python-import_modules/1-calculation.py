#!/usr/bin/python3
from calculator_1 import add, sub, mul, div #using math im didnt work?
if __name__ == "__main__":
    a = 10 # value 10 to a
    b = 5 #value 5 to a 
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
