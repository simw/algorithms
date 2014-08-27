
def swap_it(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def sort_it(lst, comp=lambda a,b: (a<b)):
    for i in range(0, len(lst)):
        for j in range(0, i):
            if comp(lst[i], lst[j]):
                swap_it(lst, i, j)

def insertion_sort(lst, comp):
    sort_it(lst, comp)
