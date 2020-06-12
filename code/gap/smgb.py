from Bio import SeqIO
def semiglobal_alignment(s, t):
    matr, prev = [[0] * (len(t) + 1) for _ in xrange(len(s) + 1)], [[0] * (len(t) + 1) for _ in xrange(len(s) + 1)]
    for j in range(len(t) + 1):
        prev[0][j] = 1
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            matr[i][j], prev[i][j] = max((matr[i - 1][j] - 1 * (j != len(t)), 0),  # (i - 1, j)),
                                         (matr[i][j - 1] - 1 * (i != len(s)), 1),  # (i, j - 1)),
                                         (matr[i - 1][j - 1] + (s[i - 1] == t[j - 1]) * 2 - 1, 2))  # (i - 1, j - 1)))
    print matr[-1][-1]
    non_recursive_trace(s, t, prev)
def non_recursive_trace(s, t, prev):
    i, j, ss, tt = len(s), len(t), "", ""
    while i > 0 or j > 0:
        if prev[i][j] == 0:
            i -= 1
            ss += s[i]
            tt += "-"
        elif prev[i][j] == 1:
            j -= 1
            ss += "-"
            tt += t[j]
        else:
            i -= 1
            j -= 1
            ss += s[i]
            tt += t[j]
    print ss[::-1]
    print tt[::-1]
f = open("/home/ralf/Downloads/rosalind_smgb.txt","r")
seqs = SeqIO.parse(f, "fasta")
seqs = [str(s.seq) for s in seqs]
semiglobal_alignment(seqs[0], seqs[1])