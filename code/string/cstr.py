lines = open("/home/ralf/Downloads/rosalind_cstr.txt","r").read().split("\n")[:-1]
for i in range(len(lines)):
	d=''
	l=''
	dic={}
	for j in lines:
		d=d+j[i]
	for j in "ATCG":
		dic[j]=d.count(j)
	dd=sorted(dic.iteritems(),key=lambda dic:dic[1],reverse=True)
	for j in d:
		if j==d[0]:
			l+="1"
		else:
			l+="0"
	if dd[1][1]>=2:
		print l