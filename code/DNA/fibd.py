line=open("/home/ralf/Downloads/rosalind_cons.txt","r").readline()
n,k=line[0],line[1]
def	rabbit(n,m):
	small={1:1,2:0}#键表示月份，值表示每个月小兔子的个数
	big={1:0,2:1}  #键表示月份，值表示每个月大兔子的个数
	if n<3:
		print"out 1 pairs rabbits "
	else:
		for j in range(3,n+1,1):#j表示月份
			if j<=m:
				small[j]=big[(j-1)]
				big[j]=small[(j-1)]+big[(j-1)]
			else:
				small[j]=big[(j-1)]
				big[j]=small[(j-1)]+big[(j-1)]-small[j-m]#大兔子包括上一个月小兔子长大+大兔子—m个月前是小兔子的数目
		print"out:\n"+str(small[j]+big[j]) +" pairs rabbit "
rabbit(n,m)