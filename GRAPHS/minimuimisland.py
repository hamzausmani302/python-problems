
#issland count


def island_count(grid ,visited):
  #search for land linearly 
  #as L appears check whether the node is in visited list
  #if it is not in visited list call the fill_island function
	#increment counter 
  #repeat till the las tnode
	nodes = [];
	counter = 0;
	lowest = 999;
	for i in range(0,  len(grid)):
		for j in range(0 , len(grid[i])):
			if(grid[i][j] == 'L' and is_visited([i,j] , visited , grid) == False):
				result = fill_island([i,j] , grid , visited , []);
				#print(result);
				if(result != []):
					if(len(result) < lowest):
						lowest = len(result);
						
					counter +=1;
					nodes.append(result);
	
	if(lowest == 999):
		return 0;
	return lowest;
	pass # todo

def is_visited(node , visited , grid):
	
	if(node[0] < 0 or node[1] < 0):
		return True;
	if(node[0] >= len(grid) or node[1] >= len(grid[0])):
		return True;

	for n in visited:
		if(node == n):
	
			return True;
	
	
	return False;		

def fill_island(node,  grid , visited= [] , comp_nodes =[]):
	
	#fetch node
	#check if neightbors are visisted
		#if not visited
			#add thgem to visited , comp_ndoes
			#island with neightbors node
	
	left= node[0];
	right = node[1];
	visited.append([left , right]);
	comp_nodes.append([left , right]);
	  
	if(is_visited([left , right+1] , comp_nodes , grid) == False and grid[left][right+1] =='L' ):
		
		fill_island([left , right+1] , grid , visited , comp_nodes);
	if(is_visited([left , right -1] , comp_nodes , grid) == False and grid[left][right-1] =='L'):
		
		
		fill_island([left , right -1] , grid , visited , comp_nodes);
	if(is_visited([left +1 , right] , comp_nodes , grid) == False and grid[left+1][right] =='L'):
		
		
		fill_island([left +1 , right], grid , visited , comp_nodes);
		
	if(is_visited([left -1 , right] , comp_nodes , grid) == False and grid[left-1][right] =='L'):
		
		
		fill_island([left -1 , right] , grid , visited , comp_nodes);
			
	return comp_nodes;	



#####			Test Cases
GRIDS = [[
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
],
 [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
],
[
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
],
[
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]
]


ans = [2,1,9,1]  ## answer for the test cases

def test():
	for i in range(0 , len(ans)):
		res = island_count(GRIDS[i] , []);
		print(res);
		if(res != ans[i]):
			print("failed at " + str(i) );
			return 1;
	print("PASSED !! BINGO");				

test();
