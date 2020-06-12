string=open("/home/ralf/Downloads/rosalind_hamm.txt","r").readlines()
print sum([a != b for a, b in zip(string[0], string[1])])