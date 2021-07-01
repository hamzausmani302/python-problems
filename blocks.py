# buying house in different blocks

blocks = [
{
"gym":  True,
"school" : False,
"store" : True
},
{
"gym":  True,
"school" : True,
"store" : False	
},
{
"gym":  False,
"school" : False,
"store" : True	
},
{
"gym":  False,
"school" : True,
"store" : False	
},
{
"gym":  False,
"school" : False,
"store" : False	
}

];

comp = [];

reqs = ["gym" , "school" , "store"];


def find_up(block ,place):
	i = block;
	cost = 0;
	while(i >=0):
		if(blocks[i][place]):
			return cost;	
		cost = cost + 1;
		i=i-1;
	return -1;
def find_below(block , place):
	i = block;
	cost = 0;
	while(i < len(blocks)):
		if(blocks[i][place]):
			return cost;	
		cost = cost + 1;
		i=i+1;
	
	return -1;

def find_nearest_for(block ):
	cost = 0;
	ucost = 0;
	dcost = 0;
	for req in reqs:
		
		if(blocks[block][req]):
			cost = cost +  0;
		else:
			distup = find_up(block , req );
			distdown = find_below(block , req);
			print( "block = " + str(block) +"   distup  = " + str(distup) + "  distdown = " + str(distdown) );
			if(distup == -1 and distdown == -1):
				pass;
			if(distup == -1):
				cost = cost + distdown;
			elif(distdown == -1):
				cost = cost + distup	
			elif(distup < distdown):
				cost = cost + distup;
			else:
				cost = cost + distdown;	
	return cost;

def form_query_dup():
	obj = {};
	for i in range(0 , len(blocks) ):
		obj = {};
		for req in reqs:
			
			value = False;
			if(blocks[i][req]):
				value = True;
			obj[req] = value
		comp.append(obj);	

			
form_query_dup();

def calc_lowest():
	least = find_nearest_for(1);
	block= 0;
	for i in range(1 , len(blocks)):
		t = find_nearest_for(i)
		if(least > t):
			least = t;
			block = i;
	return (least ,block);

least , block = calc_lowest();
print("block = "+str(block) + "least = " + str(least));	
	
