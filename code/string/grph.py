import sys
import re
import collections
lines=open("/home/ralf/Downloads/rosalind_grph.txt","r").readlines()
line=[]
q=[]
p=[]
o=[0]
for one in lines:
	one=one.strip()
	if ">" not in one:
		line=line+str(one)
	else:
		o.append(one[1:])
		p.append(line[0:3])
		q.append(line[-3:])
		line=""
p.append(line[0:3])
q.append(line[-3:])
for i in range(1,len(o)):
	for j in range(1,len(o)):
		if p[i]==q[j]:
			if i!=j:
				print o[j],o[i]
line=[]
i=-1
for one in lines:
	one=one.strip()
	if ">" in one:
		line.append(one)
		i+=1
	else:
		line[i]=line[i]+one
for i in range(len(line)):
	for j in range(len(line)):
		if line[i][14:17]==line[j][-3:]:		
			if i!=j:
				print line[j][1:14],line[i][1:14]