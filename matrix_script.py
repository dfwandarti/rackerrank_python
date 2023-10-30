# https://www.hackerrank.com/challenges/matrix-script

#!/bin/python3

import math
import os
import random
import re
import sys
import re

def matrix_script(matrix):
    str = ""
    
    for s in matrix:
        str = str + s

    temp = re.sub(r"([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])", r"\1 \2", str)
    while (temp != str):
        str = temp
        re.sub(r"([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])", r"\1 \2", str)
    return str


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = [matrix[l][c] for c in range(m) for l in range(n)]
print(matrix_script(decoded))
