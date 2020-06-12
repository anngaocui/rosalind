print ("string1:")
string1="AGTCGTAGCGTGCAGTCGTCAAAATGCATAAATTGCACTGATAGACGCATT"
print ("string2:")
string2="GCA"
def findmotif(string1,string2):
	print string1,string2
	len1=len(string1)
	len2=len(string2)
	for a in range(len1-len2+1):
			if string1[a:a+len2]==string2:
				print a-1
findmotif(string1,string2)