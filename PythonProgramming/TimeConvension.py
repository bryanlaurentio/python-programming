#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    if s[-2:] == 'PM' and hour != 12 and hour >= 1:
        hour += 12
    elif s[-2:] == 'AM' and hour == 12:
        hour = 0

    print('{hour:02d}{ms}'.format(hour = hour, ms = s[2:-2]))

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
