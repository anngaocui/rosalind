string=open("/home/ralf/Downloads/rosalind_iprb.txt","r").readline()
string=string.split(" ")
aa=int(string[0])
AA=int(string[1])
Aa=int(string[2].strip())
total=aa+AA+Aa
A=(AA*1.0/total)*((AA-1)*1.0/(total-1))*(1.0/2)+(AA*1.0/total)*(Aa*1.0/(total-1))*1.0+(AA*1.0/total)*(aa*1.0/(total-1))*1.0+(Aa*1.0/total)*((Aa-1)*1.0/(total-1))*(3.0/4)*(1.0/2)+(Aa*1.0/total)*(aa*1.0/(total-1))*(1.0/2)
a=(aa*1.0/total)*((aa-1)*1.0/(total-1))*(1.0/2)+(Aa*1.0/total)*(aa*1.0/(total-1))*(1.0/2)+(Aa*1.0/total)*((Aa-1)*1.0/(total-1))*(1.0/4)*(1.0/2)
print A/(a+A)