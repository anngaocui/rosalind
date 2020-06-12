string=[line.strip() from line in open("/home/ralf/Downloads/rosalind_subs.txt","r")]
r = 0
while r != -1 :
    r = string[0].find(string[1],r+1)
    print r+1