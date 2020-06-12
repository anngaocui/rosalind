cod=open("rnacodon.txt","r").readlines()
lines=open("/home/ralf/Downloads/rosalind_orf.txt","r").readlines()
L=""
for line in lines:#拼接序列
	if ">" in line:
		pass
	else:
		line=line.strip()
		L=L+str(line)
L=L.replace("T","U")
L1=L.replace("A","u").replace("U","a").replace("G","c").replace("C","g").upper()[::-1]#反向互补序列
codon={}#密码子字典
for line in cod:
	one=line.split("      ")
	for t in one:
		ll=t.split("   ")
		for l in ll:
			k=l.split(" ")
			codon[k[0]]=(k[1].strip())
for L in [L1,L]:#寻找开放阅读匡
	for i in range(len(L)-2):
		P=""
		if 	L[i:i+3] =="AUG":
			k=1
			while k:
				if codon[str(L[i:i+3])]=="Stop":
					print P
					break
				else:
					P=P+codon[str(L[i:i+3])]
					i=i+3
					if i+3>len(L):
						break