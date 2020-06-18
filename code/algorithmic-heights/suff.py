# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- author: Ann  -*-
# http://rosalind.info/problems/suff/

import re


def rear(file_name):
    text = open("/home/rosalind/Downloads/{}".format(file_name)).read()
    seqs = text.strip()
    # seqs = "GTCCGAAGCTCCGG$"
    result = ["$"]
    for extend_base in "ATCG":
        lines = []
        search = re.compile(extend_base).search(seqs)
        while search:
            lines.append(seqs[search.start() + 1:])
            search = re.compile(extend_base).search(seqs, search.start() + 1)
        if lines:
            out = get_end_seq(extend_base, lines)
            result.extend(out)
                # print(out)
    # print "\n".join(result)
    with open("out.txt", "w") as h:
        h.write("\n".join(result))
    print len(result)


def get_end_seq(extend_base, lines):
    result = []
    end = False
    if len(lines) == 1:
        return [extend_base+lines[0]]
    else:
        left_lines = {}
        for line in lines:
            if line[0] == "$":
                end = True
            else:
                if line[0] not in left_lines:
                    left_lines[line[0]] = [line[1:]]
                else:
                    left_lines[line[0]].append(line[1:])
    if len(left_lines.keys()) == 1:
        if left_lines.values()[0]:
            if end:
                result.append("$")
                result.append(extend_base)
                extend_base = left_lines.keys()[0]
                result.extend(get_end_seq(extend_base, left_lines.values()[0]))
            else:
                extend_base += left_lines.keys()[0]
                result.extend(get_end_seq(extend_base, left_lines.values()[0]))
        else:
            result.append(extend_base+"$")
    else:
        if end:
            result.append("$")
        result.append(extend_base)
        for extend_base in left_lines:
            result.extend(get_end_seq(extend_base, left_lines[extend_base]))
    return result

if __name__ == "__main__":
    rear("rosalind_suff.txt")