
from insertion_sort.insertion_sort import insertion_sort
from merge_sort.merge_sort import merge_sort

from random import randrange

def main():
    lst_len = 99
    funcs = [insertion_sort, merge_sort]
    comp = lambda a, b: (a < b)
    lst = [randrange(1,1e6) for i in range(0, lst_len)]
    
    res = []
    for f in funcs:
        tmp = list(lst)
        f(tmp, comp)
        print('Res: {0}'.format(tmp))
        res.append((f.__name__, tmp)) 
     
    for i in range(1, len(res)):
        for j in range(0, len(res[0][1])):
            if res[i][1][j] != res[0][1][j]:
                print('Error in {0}'.format(res[i][0]))
                continue

if __name__ == '__main__':
    main()
