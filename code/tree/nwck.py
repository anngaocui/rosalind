from Bio import Phylo
from cStringIO import StringIO
s = open('/home/ralf/Downloads/rosalind_nwck.txt','r').read().strip().split("\n\n")
s = [x.replace('\n','').split(';') for x in s]
ret = []
for n in s:
    tree = Phylo.read(StringIO(n[0]), "newick")#newick：支持的树的格式
    node1, node2 = n[1].split()
    ret.append(str(int(tree.distance({"name": node1}, {"name": node2}))))
print ' '.join(ret)