lines=open("/home/ralf/Downloads/rosalind_tran.txt","r").readlines()
ones=[]
i=-1
for line in lines:
	line=line.strip()
	if ">" in line:
		ones.append("")
		i+=1
	else:		
		ones[i]=ones[i]+line
total=sum([a != b for a, b in zip(ones[0], ones[1])])
one1=ones[1].replace("A","c").replace("G","t").replace("C","a").replace("T","g").upper()
one2=ones[1].replace("A","t").replace("G","c").replace("T","a").replace("C","g").upper()
total1=sum([(a != b and (a==c or a==d))for a, b,c,d in zip(ones[0],ones[1],one1,one2)])
print (total-total1)*1.0/(total1)