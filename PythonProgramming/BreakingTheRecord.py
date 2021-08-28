#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest = scores[0]
    lowest = scores[0]

    sum_highest = 0
    sum_lowest = 0
    for i in scores:
        if i > highest:
            highest = i
            sum_highest += 1
        elif i < lowest:
            lowest = i
            sum_lowest += 1
    print(sum_highest,sum_lowest)


if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

