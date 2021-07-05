

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
	
	
def transverse( i , j ,  endx , endy):
	
	stack = [];
	stack.append([2,3]);
	while(len(stack) != 0):
			popped = stack.pop();
			print(popped);
	

transverse(0,0  , 8,5);	
