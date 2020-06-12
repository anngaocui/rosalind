# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- author: Ann  -*-
# http://rosalind.info/problems/sort/

def rear(file_name):
    text = open("/home/ann/Downloads/{}".format(file_name)).read()
    records = text.strip().split("\n\n")
    result = []
    for record in records:
        read1, read2 = record.split("\n")
        read1 = map(int, read1.split(" "))
        read2 = map(int, read2.split(" "))
        result.append(change_index(read1, read2, 0))
    with open("out.csv", "w") as h:
        h.write(" ".join(map(str, result)))
    print result


def change_index(read1, read2, exchange=0):
    mismatch = []
    for index in range(len(read1)):
        if read1[index] != read2[index]:
            mismatch.append(index)
    result = []
    if mismatch:
        exchange += 1
        out = []
        index = mismatch[0]
        record_index = read2.index(read1[index])
        print index + 1, record_index + 1
        read22 = read2[:index] + read2[index: record_index + 1][::-1] + read2[record_index + 1:]
        out.append(change_index(read1, read22, exchange))
    else:
        result = exchange
    return result

if __name__ == "__main__":
    rear("rosalind_sort.txt")