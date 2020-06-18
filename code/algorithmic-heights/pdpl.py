# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- author: Ann  -*-
# http://rosalind.info/problems/pdpl/
from itertools import combinations
import math


def pdpl(file_name):
    ints = open("/home/rosalind/Downloads/{}".format(file_name)).read()
    # ints = "2 2 3 3 4 5 6 7 8 10"
    ints = map(int, ints.strip().split(" "))
    ints = sorted(ints)
    number = int(math.sqrt(len(ints)*2))
    select = [int_a for int_a in set(ints) if ints[-1] - int_a in ints]
    result = get_list(ints, [0, ints[-1]], sorted(select), number)
    with open("out.txt", "w") as h:
        h.write(" ".join(map(str, sorted(result[0]))))


def difs(lists):
    return [int_b-int_a for int_a, int_b in combinations(sorted(lists), 2)]


def compare_list(list1, list2):
    result = False
    for int_a in set(list1):
        if list1.count(int_a) > list2.count(int_a):
            result = True
            break
    return result


def get_list(all_lists, select_list, select, number):
    result = []
    if set(difs(select_list)).difference(set(all_lists)):
        pass
    elif compare_list(difs(select_list), all_lists):
        pass
    elif sorted(difs(select_list)) == all_lists:
        result = [select_list]
    else:
        for add_int in select:
            if len(select) - select.index(add_int) + len(select_list) >= number:
                if add_int > sorted(select_list)[-2]:
                    if all_lists[-1] - add_int in all_lists:
                        result.extend(get_list(all_lists, select_list + [add_int], select, number))
                        if result:
                            break
            else:
                break
    return result

if __name__ == "__main__":
    pdpl("rosalind_pdpl.txt")