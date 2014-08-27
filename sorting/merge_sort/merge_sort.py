from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

from math import log, ceil

def merge_it(lst1, lst2, comp):
    # Does an out-of-place merging of two lists
    # returning the result
    i1 = 0
    i2 = 0
    res = []

    while i1 < len(lst1) or i2 < len(lst2):
        if i1 == len(lst1):
            res.append(lst2[i2])
            i2 = i2 + 1
        elif i2 == len(lst2):
            res.append(lst1[i1])
            i1 = i1 + 1
        elif comp(lst1[i1], lst2[i2]):
            res.append(lst1[i1])
            i1 = i1 + 1
        else:
            res.append(lst2[i2])
            i2 = i2 + 1

    return res


def split_and_sort(lst, comp):
    if len(lst) < 2:
        return

    n = 2**int(log(len(lst)-0.5,2))

    if n > 1:
        tmp = lst[:n]
        split_and_sort(tmp, comp)
        lst[:n] = tmp 
        
        tmp = lst[n:]
        split_and_sort(tmp, comp)
        lst[n:] = tmp 

    lst[:] = merge_it(lst[:n], lst[n:], comp)

def sort_it(lst, comp):
    # Sort the list and give result in place
    split_and_sort(lst, comp) 

def merge_sort(lst, comp):
    sort_it(lst, comp)
