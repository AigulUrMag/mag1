m=[[9,70,20,67,33],[60,20,94,14,77],[27,58,45,0,13],[39,47,25,97,69],[83,13,100,1,85]]
len_m=len(m)
max=0
for i in range(len_m):
	for j in range(len_m):
		if max<m[i][j]:
			max=m[i][j]
print(max),