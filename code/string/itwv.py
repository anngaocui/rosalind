#1
def check_interweave(dna1, dna2, superstr):
	if len(superstr) == 0:
		return True
	elif dna1[0] == dna2[0] == superstr[0]:
		return check_interweave(dna1[1:], dna2, superstr[1:]) or check_interweave(dna1, dna2[1:], superstr[1:])
	elif dna1[0] == superstr[0]:
		return check_interweave(dna1[1:], dna2, superstr[1:])
	elif dna2[0] == superstr[0]:
		return check_interweave(dna1, dna2[1:], superstr[1:])
	else:
		return False
if __name__ == '__main__':
	from numpy import zeros
	ff=open('/home/ralf/Downloads/rosalind_itwv.txt',"r").read().strip()
	superstr =ff.split("\n")[0]
	dna = ff.split("\n")[1:]
	M = zeros((len(dna), len(dna)), dtype=int)
	for i in xrange(len(dna)):
		for j in xrange(len(dna)):
			if i <= j:
				current_profile = [(dna[i]+dna[j]).count(nucleotide) for nucleotide in 'ACGT']
		        for index in xrange(len(superstr)-len(dna[i])-len(dna[j])+1):
					if current_profile == [superstr[index:index+len(dna[i])+len(dna[j])].count(nucleotide) for nucleotide in 'ACGT']:
						if check_interweave(dna[i]+'$', dna[j]+'$', superstr[index:index+len(dna[i])+len(dna[j])]):
							M[i][j] = 1
							break
			else:
				M[i][j] = M[j][i]
	print '\n'.join([' '.join(map(str, M[i])) for i in xrange(len(dna))])
#2
import sys
lines = open('/home/ralf/Downloads/rosalind_itwv.txt',"r").read().strip().split("\n")
n = len(lines)-1
mat = [[0 for a in range(n)] for b in range(n)]
def can_interweave(pat, s, t):
    def test(x, i, j):
        if i == len(s) and j == len(t): return True
        if len(pat) == x: 
			return False
        v = False
        if i < len(s) and pat[x] == s[i]:
            v = test(x+1,i+1,j)
        if not v and j < len(t) and pat[x] == t[j]:
            v = test(x+1,i,j+1)
        return v
    for i in range(len(pat)):
        if test(i,0,0):
            return True
    return False
for i in range(n):
    for j in range(i,n):
        if can_interweave(lines[0],lines[i+1],lines[j+1]):
            mat[i][j] = 1
            mat[j][i] = 1
for r in mat:
    print ' '.join(map(str,r))