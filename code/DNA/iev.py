string=open("/home/ralf/Downloads/rosalind_iev.txt","r").readline()
print sum([ a*int(b) for a,b in zip([2,2,2,1.5,1,0], string.split()) ])