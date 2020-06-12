import urllib2
import re
lines=open("/home/ralf/Downloads/rosalind_mprt.txt").readlines()
for s in lines:
	s=s.strip()
	html = urllib2.urlopen('http://www.uniprot.org/uniprot/'+str(s)+'.fasta').read()
	print html   
	pro="".join(html.split('SV=')[1].split("\n"))
	index=[]
	for q in re.finditer(r'N[^P]T[^P]',pro):
		index.append(q.span()[0])
	for P in re.finditer(r'N[^P]S[^P]',pro):
		index.append(P.span()[0])
	if len(index) is not 0:
		print s
		indexs=""
		for a in sorted(index):	
			indexs=indexs+str(a)+" "
		print indexs