rna = "".join(open('/home/ralf/Downloads/rosalind_rnas.txt',"r").readline().strip())
matchings = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}
def wobble_bonding(rna):
	if len(rna) <= 3:
		return 1
	else:
		if rna in wobble_dict:
			return wobble_dict[rna]
		else:
			subintervals = []
			for i in xrange(4, len(rna)):
				if rna[0] in matchings[rna[i]]:
					subintervals.append([rna[1:i],rna[i+1:]])
			wobble_dict[rna] = (sum([wobble_bonding(subint[0])*wobble_bonding(subint[1]) for subint in subintervals]) + wobble_bonding(rna[1:]))
			return wobble_dict[rna]
wobble_dict = {}
wobble = wobble_bonding(rna)
print wobble