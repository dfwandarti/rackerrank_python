# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

if __name__ == '__main__':
    c, l = map(int, input().split())
    matrix = []
    for _ in range(c):
        matrix.append(list(map(int, input().split())))

    print(numpy.prod(numpy.sum(matrix, axis=0)))        
