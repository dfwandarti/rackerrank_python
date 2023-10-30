# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy
from numpy import dot

if __name__ == "__main__":
    n = int(input())
    a,b = [numpy.array([input().split()  for i in range(n)],int)  for _ in range(2)]
    
    print(dot(a,b))
