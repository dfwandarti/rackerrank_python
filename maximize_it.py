# https://www.hackerrank.com/challenges/maximize-it

import itertools
from functools import reduce

if __name__ == '__main__':
    k, m = map(int, input().split(' '))
    lists = []
    for l in range(k):
        lists.append(list(map(int, input().split(' ')))[1:])
     
    
    all_sums = []
    combinations = list(itertools.product(*lists))
    for combi in combinations:
        all_sums.append(reduce(lambda a, b: a + b * b, combi, 0))
        
        all_sums.append(reduce(lambda a, b: a + b * b, combi, 0) % m)

    print(max(list(filter(lambda s: s < m, all_sums))))
