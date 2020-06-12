line=open("/home/ralf/Downloads/rosalind_mrna.txt").readline()
pro=""
pro=line.strip()
E=pro.count("I")
D=sum(pro.count(i) for i in ["w","M"])
A=sum(pro.count(i) for i in ["L","R","S"])
B=sum(pro.count(i) for i in ["P","V","A","G","T"])
C=sum(pro.count(i) for i in ["Y","E","D","K","H","F","N","C","Q"])
print (3**E)*(6**A)*(4**B)*(2**C)*3%1000000