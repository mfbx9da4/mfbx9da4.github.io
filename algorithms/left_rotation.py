#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    ind = d % len(a)
    end = a[ind:]
    beg = a[:ind]
    return end + beg

if __name__ == '__main__':

    n = 5
    d = 4
    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)

    print(result)
