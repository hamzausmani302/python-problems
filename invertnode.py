
#invert nodes of tree
#symmetric tree generation

def print1(root):
	if(root== None):
		return 1;
	print(root.value);
	if(root.right == None and root.left == None):
		return 1;
		
	if(root.left != None):
		print1(root.left);
	if(root.right != None):
		print1(root.right);

def invert(root):
	if(root== None):
		return 1;
	temp = root.left;
	root.left=  root.right;
	root.right = temp;
	
	if(root.right == None and root.left == None):
		return 1;
	
	if(root.left != None):
		invert(root.left);
	if(root.right != None):
		invert(root.right);

class NODE:
	def __init__(self ,value=0 , next1=None , next2 = None):
		self.value = value;
		self.right = next1;
		self.left = next2;
	

class BinaryT:
	def __init__(self):
		self.root = None;
		
	def add_node(self , node):
		if(self.root == None):
			self.root = node;
		else:
			self.insert_node( self.root , node)
				
	def insert_node(self , nodes , q):
		
		if(nodes.right == None and q.value > nodes.value  ):
			nodes.right = q;
			
		elif(nodes.left == None and q.value < nodes.value  ):
			nodes.left = q;
			
		elif(nodes.right != None and q.value > nodes.value):
			self.insert_node(nodes.right , q);
		elif(nodes.left != None and q.value < nodes.value):
			self.insert_node(nodes.left , q);
				

tree = BinaryT();
tree.add_node(NODE(100));
tree.add_node(NODE(115));
tree.add_node(NODE(120));
tree.add_node(NODE(117));
tree.add_node(NODE(29));
tree.add_node(NODE(16));

tree.add_node(NODE(25));

tree.add_node(NODE(23));

tree.add_node(NODE(27));
tree.add_node(NODE(14));
print1(tree.root);
print("");
invert(tree.root);
print1(tree.root);
