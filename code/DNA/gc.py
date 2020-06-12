try:
	string=open("/home/ralf/Downloads/rosalind_gc.txt","r").readlines()
except:
	print "file was Error"
GC=total=0
ql={}
for line in string:
	line.strip()
	if ">" in line:
		if total >0:
			ql[ll]=GC*0.1/total*1000
			GC=total=0
		ll=str(line.split(">")[1])
	else:
		GC=GC+line.count("G")+line.count("C")
		total=total+len(line)#line.count("G")+line.count("C")+line.count("T")+line.count("A")
ql[ll]=GC*0.1/total*1000
print sorted(ql.iteritems(),key=lambda ql:ql[1],reverse=True)[0][0].strip()
print sorted(ql.iteritems(),key=lambda ql:ql[1],reverse=True)[0][1