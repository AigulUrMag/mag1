l=[1,4,1,6,"hello","a",5,"hello"]
l_unic=[]
for i in l:
	if i not in l_unic:
		l_unic.append(i)
print(l_unic)