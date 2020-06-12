rna = "".join(open('/home/ralf/Downloads/rosalind_cat.txt',"r").read().strip().split("\n")[1:])
def noncrossing_perfect_bondings(rna):
	bonding = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
	noncrossing_bondings = {}
	def count_noncrossing(rna):
		if len(rna) <= 2: 
			return 1
		elif rna in noncrossing_bondings: 
			return noncrossing_bondings[rna]
		splits = [i for i in xrange(1, len(rna), 2) if rna[0] == bonding[rna[i]] and check_subinterval(rna[1:i])]
		noncrossing_bondings[rna] = sum([count_noncrossing(rna[1:i])*count_noncrossing(rna[i+1:]) for i in splits]) % 1000000
		return noncrossing_bondings[rna]
	return count_noncrossing(rna)
def check_subinterval(subint):
	N = [subint.count(nucleotide) for nucleotide in 'AUCG']
	return N[0] == N[1] and N[2] == N[3] 
noncrossing = str(noncrossing_perfect_bondings(rna))
print noncrossing
#short one
c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}
def catalan(s):
    if s not in c:
        c[s] = sum([catalan(s[1:k]) * c[s[0]+s[k]] * catalan(s[k+1:]) for k in range(1, len(s))])
    return c[s]
print catalan(rna) % 10**6