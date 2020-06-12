lines= open('/home/ralf/Downloads/rosalind_eval.txt','r').readlines()
dna=lines[1].strip()
gc=dna.count("G")+dna.count("C")
at=len(dna)-gc
print " ".join([(str((0.5*i)**gc*(0.5-i/2)**at*(int(lines[0].strip())-len(dna)+1)))for i in map(float,lines[2].strip().split(" "))])