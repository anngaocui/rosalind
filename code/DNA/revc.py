
string=open("/home/ralf/Downloads/rosalind_revc1.txt","r").readline()
from string import maketrans
print(string[::-1].translate(maketrans('ACGT', 'TGCA')))