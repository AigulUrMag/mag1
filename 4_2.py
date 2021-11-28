def sort(a) :
	n=len(a)
	for i in range(0,n):
		for j in range(i,0,-1):
			if a[j]< a[j-1]:
				a[j],a[j-1]=a[j-1],a[j]
			else:
				break
	

a=[50,35,28,19,45,8,89,91,10,125]

r=sort(a)
print('Отсортированный массив',a)
