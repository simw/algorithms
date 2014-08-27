from __future__ import absolute_import

from merge_sort.merge_sort import merge_sort
from insertion_sort.insertion_sort import insertion_sort

from random import randrange
import time

def timeit(f):
    def wrapper(*args, **kwargs):
        t1 = time.clock()
        res = f(*args, **kwargs)
        t2 = time.clock()
        tdiff = round((t2-t1)*1000, 3)
        return res, tdiff, f.__name__
    return wrapper

def run_it(f, n):
    lst = [randrange(1,1e6) for i in range(0, n)]
    comp = lambda a, b: (a < b)
    timed_sort = timeit(f)
    res = timed_sort(lst, comp) 

    return res[1]

def main():
    funcs = [insertion_sort, merge_sort]
    lens = (12, 17)

    ns = [[2**n for n in range(0,l)] for l in lens]

    print('algorithm,length,time')
    for i in range(0, len(funcs)):
        f = funcs[i]
        res = [(n, run_it(f, n)) for n in ns[i]]

        for r in res:
            print('{0},{1},{2}'.format(f.__name__, r[0], r[1]))
    
if __name__ == '__main__':
    main()
