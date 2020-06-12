lines=open("/home/ralf/Downloads/rosalind_lcsq.txt","r").readlines()
import re
f=open("lo.txt","w")
ones=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line
a=ones[0]
b=ones[1]
print len(ones[0])
print len(ones[1])
g=[]
j=0
for i in range(len(a)):
	if a[i]==b[j]:
		g.append(a[i])
		j+=1
	elif a[i]==b[j+1]:
		g.append(a[i])
		j=j+2
	elif a[i]==b[j+2]:
		g.append(a[i])
		j=j+3
print "".join(g)