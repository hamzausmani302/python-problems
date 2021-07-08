

count = 0;
grid = [];
def make_grid():
	for i in range(0, 9):
		arr =[];
		for j in range(0,6):
			arr.append((i*6 + j));
			
		grid.append(arr);

make_grid();
for i in grid:
	print(i);
	
def decison(i , j , endx , endy):
	x_diff = i-endx;		#+ve  endx kai agay  #-ve 
	y_diff = j-endy;
	if(x_diff < 0 and grid[i][j+1] != 0):
		#go right
		return 1;
	if(y_diff < 0 and grid[i+1][j] != 0):
		#go downw
		return 2;	
	if(x_diff > 0 and grid[i][j-1] != 0):
		#go left
		return 3;
	if(y_diff > 0 and grid[i-1][j] != 0):
		#go up
		return 4;

results = [];
	
def transverse( i , j ,  endx , endy):
	
	stack = [];
	resstack = [];
	stack.append([i,j]);
	while(len(stack) != 0):
		
			popped = stack.pop();
			print(popped);
			if(popped[0] == endx and popped[1] == endy):
				print("reached");
				results.append(resstack);
			#return 1;
			else:
				resstack.append(popped);
		
				prev = [-1,-1];	
				if(len(resstack) > 2 ):
					prev= resstack[len(resstack)-2]
				print("prev" + str(prev))
			
				if(popped[1]+1 < 6 and (popped[0] != prev[0] or popped[1]+1 != prev[1])):
				#right
					stack.append([popped[0] , popped[1]+1]);
				if(popped[0]+1 < 9 and (popped[0]+1 != prev[0] or popped[1] != prev[1])):
				#down
					stack.append([popped[0]+1 , popped[1]]);
		
				
				if(input("?")==-1):
					for col in results:
						print(col);
				else:
					print(stack);
					print(resstack);
					
		#d = decision(popped[0] , popped[1] . endx ,endy);	
		
		
		
		#grid[popped[0]][popped[1]] = 1;
		
		
		
		
	

transverse(0,0  , 8,5);	
print(results);
