#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max_arr = max(arr)
    min_arr = min(arr)

    # min = arr.remove(max_arr)
    # max = arr.remove(min_arr)

    sum_min = 0
    sum_max = 0

    for i in arr:
        sum_min += i
    for j in arr:
        sum_max += j
    print(sum_min-max_arr, sum_max-min_arr)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
