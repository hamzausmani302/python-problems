
#reversing a linkew list problem solution

class NODE:
	def __init__(self ,value=0 , next1=None):
		self.value = value;
		self.next = next1;
	

def rev(prev , thisnode):
	
	if(thisnode == None):
		return prev;
	print(str(prev.value)  +  "    "  + str(thisnode.value));
	next1 = thisnode.next;
	thisnode.next = prev;
	rev(thisnode , next1);
		

def reverse(list12):
	last = list12.find_end();
	node = rev(list12.head , list12.head.next);
	list12.head.next = None;
	list12.head = last;
	list12.print1();
	pass;	
	
class linklist:
	def __init__(self):
		self.head = None;
		pass;
	def find_end(self):
		if(self.head == None):
			return None;
		n = self.head;
		while(n.next != None):
			n = n.next;
			pass;
		return n;	
			
		
	def add_node_end(self , node):
		if(self.head ==None):
			self.head = node;
			return node;
		last = self.find_end();
		
		last.next = node;
		return node;
			
		pass;	
	def print1(self):
		n = self.head;
		while(n != None):
			print(n.value);
			n=n.next;
			
		
list1 = linklist();
list1.add_node_end(NODE(1));

list1.add_node_end(NODE(2));


list1.add_node_end(NODE(3));
list1.add_node_end(NODE(4));
list1.add_node_end(NODE(18));
list1.print1();	
reverse(list1);
