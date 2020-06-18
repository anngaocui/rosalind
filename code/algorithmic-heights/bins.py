# -*- coding: utf-8 -*-

def bins():
    lines = open("/home/rosalind/下载/rosalind_bins.txt", "r").readlines()
    n = int(lines[0].strip())
    m = int(lines[1].strip())
    a = lines[2].strip().split(' ')
    k = lines[3].strip().split(' ')
    a_list = {}
    for i in xrange(1, n+1):
        a_list[a[i-1]] = i
    out = [a_list[j] if j in a_list else -1 for j in k]
    return out

if __name__ == "__main__":
    out = bins()
    handle = open('rosalind_bins_out.txt', 'w')
    handle.write(' '.join(map(str, out)))
    # print out