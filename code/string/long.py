lines=open("/home/ralf/Downloads/rosalind_long.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line.strip()
one1=ones[0]
a=len(ones)
while a:
	b=1
	print one1
	for one2 in ones:
		print one2
		if one2 in one1:
			continue
		else:
			j=len(one2)/2
			while j<len(one1):
				if one1[-j:]==one2[:j]:
					one1=one1+one2[j:]
					b=0
					break
				elif one1[:j]==one2[-j:]:
					one1=one2+one1[j:]
					b=0
					break
				else:
					j+=1
		if b==0:
			break		
	a-=1		
print one1