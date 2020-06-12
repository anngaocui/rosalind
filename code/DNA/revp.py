import re
lines=open("/home/ralf/Downloads/rosalind_revp.txt","r").readlines()
L=""
for line in lines:
	if ">" in line:
		pass
	else:
		line=line.strip()
		L=L+line
for i in range(len(L)-3):
	r=12
	while r>3:
		if i+r>len(L):
			r=r-2
		else:
			one=str(L[i:i+r])
			rev=one.replace("A","t").replace("G","c").replace("C","g").replace("T","a").upper()[::-1]
			if one==rev:
				print i+1,r
				break
			else:
				r=r-2
print len(L)