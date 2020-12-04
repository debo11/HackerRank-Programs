#!/bin/python3

import sys


input1 = int (input ())
if 1 <= input1 <= 100000:
    list1 = []
    for i in range (0, input1):
        list1.append (int (input ()))
        sum = 0
        for i in list1:
            if 1 <= i <= 1000000000:
                for z in range (0, i):
                    if z % 3 == 0 or z % 5 == 0:
                        sum = sum + z
            print (sum)
            list1.clear ()

