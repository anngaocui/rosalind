f = open("/home/ralf/Downloads/rosalind_kmp.txt","r")
seq = f.read().strip()
def kmp(seq):
    m = len(seq)
    kmpNext = m * [0]
    j = kmpNext[0]
    for i in range(1,m):
        while j > 0 and seq[i] != seq[j]:
            j = kmpNext[j-1]
        if seq[i] == seq[j] : 
            j = j + 1
        kmpNext[i] = j
    return kmpNext
tab = kmp(seq)
output = open("res_kmp.txt","w")
output.writelines( "%s " % item for item in tab )
output.close()