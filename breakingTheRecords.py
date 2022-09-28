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
    currHi = scores[0]
    currLow = scores[0]
    hiCount = 0
    lowCount = 0
    
    for score in scores:
        if score >currHi:
            currHi=score
            hiCount+=1
        elif score < currLow:
            currLow=score
            lowCount +=1
    return [hiCount, lowCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
