from decimal import Decimal
pro=open("prot_weight.txt","r").readlines()
prot={}
for i in pro:
	l=i.split("   ")
	prot[l[0]]=l[1].strip()
input_data=open('/home/ralf/Downloads/rosalind_prsm.txt')
n = int(input_data.readline())
protein = [input_data.readline().strip() for repeat in xrange(n)]
weights = sorted([Decimal(line.strip()) for line in input_data.readlines()])
def get_weight(pro,prot):
	w = 0
	for p in pro:
		w += Decimal(prot[p])
	return w
max_mult = -1
for p in protein:
	current_weights = sorted([Decimal(get_weight(item,prot)) for i in xrange(1, len(p)) for item in (p[i:],p[:-i])] + [Decimal(get_weight(p,prot))])
	multiset = {}
	for cur in current_weights:
		for given in weights:
			if round(cur - given, 3) not in multiset:#round(float,ndig=0) round(9.4636,3)->9.464
				multiset[round(cur - given, 3)] = 1
			else:
				multiset[round(cur - given, 3)] += 1
	current_mult = max(multiset.values())
	if current_mult > max_mult:
		max_mult = current_mult
		max_protein = p
max_parameters = [str(max_mult), max_protein]
print '\n'.join(max_parameters)