#from Bio.Seq import Seq	
with open('/home/ralf/Downloads/rosalind_dbru.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]
DBG_edge_elmts = set()
for kmer in k_mers:
	DBG_edge_elmts.add(kmer)
#	seq=Seq(kmer)
#	kmer=seq.reverse_complement()
#	DBG_edge_elmts.add(kmer)
	DBG_edge_elmts.add(kmer[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper())
k = len(k_mers[0])
edge = lambda elmmt: '('+elmt[0:k-1]+', '+elmt[1:k]+')'
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]
ff=open("dbru.txt","w")
ff.write('\n'.join(DBG_edges))