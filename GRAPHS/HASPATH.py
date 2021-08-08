

GRAPH = {
	'v' : ['x' ,'w'],
	'w': [],
	'x': [],
	'y': ['z'],
	'z': [],
	
	
}
#f g i
 #   g i  
def is_visited(node , visited):
	for i in range(0,len(visited)):
		if(node == visited[i]):
			return True;
	return False;
def transverse_dfs(src ,dest , visited = []):
	
	if(src == dest):
		return True;
	
	if(is_visited(src , visited) == False):
		
		visited.append(src);
		for i in range(0 , len(GRAPH[src])):
			if(transverse_dfs(GRAPH[src][i] , dest , visited) == True):
				return True;
		#if node  not visited
			# call rescursion for children
		
	
	
	return False;
print(transverse_dfs('v' , 'z' ))
