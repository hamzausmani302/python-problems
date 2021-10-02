


def checkKey(dict1, key):
	if key in dict1:
		return True;
	return False
        
def graph_maker():
	n = int(input(""));
	obj = {};
	
	for i in range(0 , n-1):
		data = input("");
		data = data.split(" ");
		if(checkKey(obj , int(data[0])) == False):
			obj[int(data[0])] = [];
		if(checkKey(obj , int(data[1])) == False):
			obj[int(data[1])] = [];
			
		obj[int(data[0])].append(int(data[1]));
	
	order = input("");
	order = order.split(" ");
	orders=  [];
	for i in range(0 , len(order)):
		orders.append(int(order[i]));	
		
		
	return (obj , n , orders);
def sort(arr ,  comp_arr):
	
	pass;
	
def transverse(obj, visited , curr,  nnodes , ordered , res):
	#print(curr , visited);
	res.append(curr);
	if curr in visited:
		pass;
	else:
		visited.append(curr);
	if curr in ordered:
				index = ordered.index(curr);
				if(index+1 < len(ordered)):
					if ordered[index+1] in visited:
						return -1;
	if(len(visited) >= nnodes and curr == 1):
		return 1;
	else:
		for i in range(0 , len(obj[curr])):
			#external here
			
			
			d= transverse(obj ,visited , obj[curr][i] , nnodes , ordered , res);
			print("d=" ,d);
			if(d==-1):
				return -1;
			if curr in ordered:
				index = ordered.index(curr);
				
				if(index+1 < len(ordered)):
					if ordered[index+1] in visited:
						
						return -1;
			res.append(curr);
			#external code here
			
	return 1;		


def compute(graph , n , order):
	v = [];
	res=[];
	#print(graph)

	result = transverse(graph , v , 1 ,n ,orders,res );
	if(result != -1):
		print(res);
		ans  = "";
		for x in res:
			ans += str(x);
			ans += " ";
		print(ans);
	else:	
		print(-1);

	
graph ,n , orders= graph_maker();
print(graph);
compute(graph , n , orders);
