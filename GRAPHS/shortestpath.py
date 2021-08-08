#shortest PAth

class QUEUE:
	def __init__(self):
		self.queue = [];
	def enqueue(self,el):
		self.queue.append(el);
	def top(self):
		if(len(self.queue) > 0):
			return self.queue[0];
		return None;	
	def dequeue(self):
		if(len(self.queue) > 0):
			self.queue.pop(0);
	def show(self):
		for el in self.queue:
			print(el);		
	def empty(self):
		if(len(self.queue) > 0 ):
			return False;
		return True;			
def is_already_there(node , graph):
	for key, value in graph.items():
		if(key == node):
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


def is_visited(node , visited):
	for i in range(0,len(visited)):
		if(node == visited[i]):
			return True;
	return False; 
def shortest_path(graph, src, dest , storage = {} , completed = []):
	
	#create a queue
	q = QUEUE();
	#push the first node
	q.enqueue(src);

	storage[src] = 0;
	#while looo[ start end when queue is empty
	while(q.empty() == False):		
			#dequeue the node
		top = q.top();
		
		q.dequeue();
		if(top != None):
			
			for i in range(0 , len(graph[top])):
				
				newd = storage[top];
				newd +=1;
				if(is_visited(graph[top][i] , completed) == False):
					
					q.enqueue(graph[top][i])
					
					if(newd < storage[graph[top][i] ]):
						storage[graph[top][i]] = newd;
		
			#push neightbors into queue update the path of neighbors
					#if distance is less than storage[i]
						#update the distance value or else leave it as it is

			completed.append(top);
		else:
			break;	
	
	if(storage[dest] == 999):
		return -1;
	return storage[dest];	
	

	
 
def get_keys(graph):
	obj = {};
	for keys in graph:
		obj[keys] = 999;
	return obj;
	
GRAPH1 = {};

EDGES = [[
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
,
 [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
],

 [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
],

 [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
],
 [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
],
[
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]
,
[
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
],
[
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]
]
args = [

['w','z'],
['y','x'],
['a','e'],
['e','c'],
['b','g'],
['w','e'],
['n','e'],
['m','s'],
]

ans = [2,1,3,2,-1,1,2 ,6]
def check_shortest(edges , GRAPH , src ,dest):
	
	make_graph(edges , GRAPH)
	storage = get_keys(GRAPH)
	completed = [];
	
	res=  shortest_path(GRAPH, src, dest , storage,completed) # -> 2
	return res;
def test():
	for i in range(0 , len(EDGES)):
		test = check_shortest(EDGES[i] , {}, args[i][0] , args[i][1]);
		print(test);
		if(test != ans[i]):
			print("failed at " + str(i) + " test");
			return 1;
	print("Success");	
test();
