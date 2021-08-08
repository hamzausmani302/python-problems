
Edges = [
['B' , 'A'],
['C' , 'A'],
['B' , 'C'],
['Q' , 'R'],
['Q' , 'S'],
['Q' , 'U'],
['Q' , 'T'],

]

GRAPH = {};
def is_already_there(node , graph):
	for key, value in graph.items():
		if(key == node):
			return True;
	return False;	
def is_visited(node , visited):
	for i in range(0,len(visited)):
		if(node == visited[i]):
			return True;
	return False;	
def make_graph(edges , graph):
	#check if node is already in object
	for i in range(0 , len(edges)):
		if(is_already_there(edges[i][0] , graph) == False):
			
			graph[edges[i][0]] = [];
		
			graph[edges[i][0]].append(edges[i][1]);
			
			if(is_already_there(edges[i][1] , graph) == False):
				graph[edges[i][1]] = [];
			graph[edges[i][1]].append(  edges[i][0]);	
		else:
			graph[edges[i][0]].append(edges[i][1]);
			if(is_already_there(edges[i][1] , graph) == False):
				graph[edges[i][1]] = [];

			graph[edges[i][1]].append(edges[i][0]);

def transverse_bfs(src ,dest , visited = []):
	pass;
def transverse_dfs(src , dest , visited = []):
	
	#print(src);
	if(src == dest):
		return True;
	
	if(is_visited(src , visited) == False):
		
		visited.append(src);
		for i in range(0 , len(GRAPH[src])):
			if(transverse_dfs(GRAPH[src][i] , dest , visited) == True):
				return True;
	return False;	

make_graph(Edges , GRAPH);
for x in GRAPH:
	print(x +  "   " + str(GRAPH[x]));
			
print("");

test_case =[ ['a', 'b'] , ['a' , 'c'] , ['r','t'] ,['r','b']  ];
result = [True , True , True , False ];
success = "passed";


# test cases from   url =  >   https://structy.net/problems/undirectected-graphs
def test():
		for i in range(0,len(test_case)):
			v1 = [];
			res = transverse_dfs(test_case[i][0].upper() , test_case[i][1].upper() , v1);
			print(test_case);
			if(res != result[i]):
			#	print(test_case[i][0].upper() + " - "+  test_case[i][1].upper()  +"  -> fail at " + str(i) + "result = "+str(res) + "  expected = " + str(result[i]) );
				return 1;
		
		
		print(success);

test();

