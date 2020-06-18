# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- author: Ann  -*-
# http://rosalind.info/problems/rear/


def rear(file_name):
    text = open("/home/rosalind/Downloads/{}".format(file_name)).read()
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
    if exchange > 10:
        result = 11
    elif mismatch:
        exchange += 1
        out = []
        for index in mismatch:
            record_index = read2.index(read1[index])
            if index < record_index:
                for record_index in range(index+1, mismatch[-1] + 1):
                    read22 = read2[:index] + read2[index: record_index + 1][::-1] + read2[record_index + 1:]
                    new_mismatch = [i for i in range(len(read1)) if read1[i] != read22[i]]
                    if not new_mismatch or max(new_mismatch) - min(new_mismatch) < max(mismatch) - min(mismatch):
                        out.append(change_index(read1, read22, exchange))
        if out:
            result = min(out)
        else:
            result = 11
    else:
        result = exchange
    return result

if __name__ == "__main__":
    rear("rosalind_rear.txt")

