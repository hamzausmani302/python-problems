

store= {};

def isexist(key):
	for k in store:
		if(key == k):
			return True;
	return False;
	
def fib_nth(i):
	if(i <= 1):
		return 1;  
	else:
		
		x= 0;
		y= 0;
		if(isexist(i-1)):
			x = store[i-1];
		else:
			x = fib_nth(i-1);
		
		if(isexist(i-2)):
			y = store[i-2];
		else:
			y = fib_nth(i-2);
		
		store[i-1] = x;
		store[i-2] = y;		
		return x + y;
		
print(fib_nth(100));		
print(store);
