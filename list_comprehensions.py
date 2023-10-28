# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

import math 
if __name__ == '__main__':
    i = int(input())
    j = int(input())
    k = int(input())
    n = int(input())        
    print([[x, y, t] for x in range(i + 1) for y in range(j + 1) for t in range(k + 1) if x + y + t != n])
