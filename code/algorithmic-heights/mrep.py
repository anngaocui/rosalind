# -*- coding: utf-8 -*-
# !/usr/bin/python
# -*- author: Ann  -*-
# http://rosalind.info/problems/mrep/
import numpy as np
import copy


def mrep(file_name):
    _seq = open("/home/rosalind/Downloads/{}".format(file_name)).read().strip()
    # _seq = "TAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTATTATATAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTAT"
    window_size = 20
    result = match_two_seq(_seq, 1, window_size)
    result = sorted(result)
    combine_span = []
    print result
    while result:
        one_span = result[0]
        out = [copy.deepcopy(one_span)]
        last_span = copy.deepcopy(one_span)
        last_span[0] += 1
        last_span[1] += 1
        while last_span in result:
            out.append(copy.deepcopy(last_span))
            one_span[2] += 1
            last_span[0] += 1
            last_span[1] += 1
        result = [span for span in result if span not in out]
        combine_span.append(one_span)
    sub_seqs = []
    print combine_span
    with open("out.txt", "w") as h:
        for span in combine_span:
            sub_seq = _seq[span[0]-2: span[0]+span[2]-2]
            if sub_seq not in sub_seqs:
                h.write(sub_seq + "\n")
                print sub_seq
                sub_seqs.append(sub_seq)
    return combine_span


def match_two_seq(_seq, seq_start, window_size):
    plot_result = []
    f_scores = np.zeros((len(_seq) + 1, len(_seq) + 1))
    for i in range(len(_seq)):  # 判断对应碱基是否一样
        for j in range(i + 1, len(_seq)):
            if _seq[i] == _seq[j]:
                f_scores[i + 1][j + 1] = f_scores[i][j] + 1
    array_start1 = window_size
    array_end2 = len(_seq) - window_size + 1
    f_score = f_scores[array_start1:, array_start1:] - f_scores[:array_end2, :array_end2]
    f_res = np.where(f_score == window_size)  # 找出window_size长度的数据
    for i, j in zip(f_res[0], f_res[1]):  # 获取一致的序列位置
        if i < j:
            plot_result.append([i + seq_start + 1, j + seq_start + 1, window_size])
    return plot_result

if __name__ == "__main__":
    mrep("rosalind_mrep.txt")
