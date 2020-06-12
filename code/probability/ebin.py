N,l=open('/home/ralf/Downloads/rosalind_ebin.txt',"r").read().strip().split("\n")
p=[int(N)*float(i) for i in l.split(" ")]
print " ".join(map(str,p))