lines=open("/home/ralf/Downloads/rosalind_mmch.txt","r").readlines()[1:]
line=''
for one in lines:
	line=line+one.strip()
a,b=sorted([line.count("A"),line.count("U")])
c,d=sorted([line.count("C"),line.count("G")])
print a,b,c,d
sun1=1
for i in range(b-a+1,b+1):
	sun1=sun1*i
for i in range(d-c+1,d+1):
	sun1=sun1*i
print sun1