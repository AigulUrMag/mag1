def search1(a,key) :
	i=0
	n=len(a)-1
	while i<=n:
		m=int(i+(n-1)/2)
		#print(m,i,n)
		if a[m]==key:
			return m
			i=n
		if a[m]>key:
			n=m-1
		else :
			i=m+1
	return -1
	

a=[1,5,8,9,45,78,89,95,101,125]
key=1
r=search1(a,key)
if r!=-1:
	print('Искомый элемент находится в строке с индексом',r)
else:	
	print('Элемент не найден')
