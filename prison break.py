

def is_wall(val1,val2,a,b):
	if(val1 == 0 or val1 == a-1):
		return True;
	if(val2 == 0 or val2 == b-1):
		return True;
	return False;
def compute(a,b):
	count = 0;
	return a*b;
	

n = int(input(""));
for i in range(0,n):
	d = input("");
	d= d.split(' ');
	print(compute(int(d[0]) , int(d[1])));	
			
					
