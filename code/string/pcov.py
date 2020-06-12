dnas = open('/home/ralf/Downloads/rosalind_pcov.txt').read().rstrip().split('\n')
cir, l = dnas[0], len(dnas[0])
dnas.remove(dnas[0])
while dnas:
    for dna in dnas:
        if dna[:-1] in cir[1:]:
            cir+=dna[-1]
            dnas.remove(dna)
output = cir[:-l+1]
print output