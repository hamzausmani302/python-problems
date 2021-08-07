

tree = [];

def make_tree(str1):
	temp = [];
	for i in str1:
		if(i == '0'):
			tree.append([0]);
		if(i=='1'):
			tree.append([1]);
		if(i == '?'):
			tree.append([0,1]);
					
def transverse(root , i , t , n):
	if(root==n):
		print("end")
		return  1;
	if( i == len(t[root])):
		print("breal")
		return 1;
	
	for j in range(0 , len(t[root])):
		transverse(root, i+1 , t , n);
	print(t[root][i]);
	transverse(root+1 , 0, t , n ); 			
	return 1;
	#if root == n return
	#if i == len(t[root]) return
	#print node at t[root][i]
	#transverse i+1 at root
make_tree("1?0???1001");	
#for i in tree:
#	print(i);	
transverse(0 , 0,tree ,len(tree));	

					
