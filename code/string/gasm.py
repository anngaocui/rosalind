k_mers=open('/home/ralf/Downloads/rosalind_gasm.txt',"r").read().strip().split("\n")
for kval in xrange(1,len(k_mers[0])):
	DBG_edge_elmts = set()
	for kmer in k_mers:
		for i in xrange(kval):
			DBG_edge_elmts.add(kmer[i:len(kmer)+i-kval+1])
			#print kmer[i:len(kmer)+i-kval+1],"ing1"
			DBG_edge_elmts.add((kmer[i:len(kmer)-kval+i+1]).replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()[::-1])
			#print (kmer[i:len(kmer)-kval+i+1]).replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()[::-1],"ing2"
	k = len(list(DBG_edge_elmts)[0])
	edge = lambda elmmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]
	cyclics = []
	for repeat in xrange(2):
		temp_kmer = DBG_edges.pop(0)
		cyclic = temp_kmer[0][-1]
		while temp_kmer[1] in [item[0] for item in DBG_edges]:
			cyclic += temp_kmer[1][-1]
			[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp_kmer[1]]
			temp_kmer = DBG_edges.pop(index)
		cyclics.append(cyclic)
	if len(DBG_edges) == 0:
		break
print cyclics[0]