s=open("/home/ralf/Downloads/rosalind_tree.txt","r").readlines()
print int(s[0]) - len(s[1:]) - 1
n=s[0].strip()
print int(n)-len(s)