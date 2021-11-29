graph ={'1':set(['2','3']),
'2':set(['4','5']),
'4':set([2])	,
'5':set([2]),	
'3':set(['6','7']),
'7':set([3]),
'6':set(['8','9']),
'8':set([6]),
'9':set([6])}

def bfs(graph,start,visited):
	queue=[]
	visited.append(start)
	queue.append(start)
	while queue:
		s=queue.pop(0)
		for v in graph[s]:
			if v not in visited:
				visited.append(v)
				queue.append(v)
			#	print(visited,queue)
						

visited=[]
print(bfs(graph,'1',visited))
