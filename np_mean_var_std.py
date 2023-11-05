# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

if __name__ == '__main__':
    c, l = map(int, input().split())
    matrix = []
    for _ in range(c):
        matrix.append(list(map(int, input().split())))

    print(numpy.mean(matrix, axis=1))
    print(numpy.var(matrix, axis=0))
    print(round(numpy.std(matrix, axis=None), 11))
