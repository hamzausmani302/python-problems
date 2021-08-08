
def is_visited(node , visited):
	for i in range(0,len(visited)):
		if(node == visited[i]):
			return True;
	return False;

def is_a_component(graph , node , visited=  [] , comp_nodes=  [] ):			#returns the list of componenet nodes;
	#if node is not in visited
	#push node to visited
	
	#print(node);
	
	if(is_visited(node , comp_nodes) == False and is_visited(node , visited) == False):
		
		comp_nodes.append(node);
		visited.append(node);
		for i in range(0,len(graph[node])):
			
			is_a_component(graph , graph[node][i] , visited ,comp_nodes  );
	return comp_nodes;	
def get_keys(graph):
	arr = [];
	for keys in graph:
		arr.append(keys);
	return arr;
def count_components(GRAPH):
	keys = get_keys(GRAPH);
	
	#iterate thoright the list of nodes
	counter = 0;
	# at 0 call is_a_componenet
	start = 0;
	v=  [];
	n = 0;
	while(len(v) != len(GRAPH)):
		c = [];
		
		component = is_a_component(GRAPH , keys[start]  , v , c);
		if(component != []):
			n += 1;
			print(component);
		
		start+=1;
		
	return n;		
	#returned is an array put the nodes into result_array;
	#end the process unitl all nodes are treversed as i  === number ofnodes
	
cases = [{
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
},
{
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
},
{},
{
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}];
res = [1,3,0,5]
	
def test():
	for i in range(0,len(cases)):
		

		total = count_components(cases[i]);
		print(str(total) + "    -   " + str(res[i]));
		if(total != res[i]):
			print("failed at test  " + str(i));	
	print("suyccess");

test();
