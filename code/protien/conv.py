lines=open("/home/ralf/Downloads/rosalind_conv.txt","r").readlines()
S1=map(float,lines[0].strip().split())
S2=map(float,lines[1].strip().split())
spectral={}
for s1 in S1:
	for s2 in S2:
		element = str(s1 - s2)
		if element in spectral:
			spectral[element] += 1
		else:
			spectral[element] = 1
smax=sorted(spectral.iteritems(),key=lambda spectral:spectral[1],reverse=True)
print str(smax[0][1])+"\n"+smax[0][0]