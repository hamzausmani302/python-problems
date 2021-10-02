

chars=  [];
def contain1(list1 , el):
	if (len(list1) ==0):
		return False;
	for i in range(0, len(list1)):
		if (list1[i] == el):
			return True;
	return False;
def find_path(string):
	alph = [];
	
	strlen = len(string)-1;
	while(strlen >= 0):
		if(contain1(alph , string[strlen]) == False):
			alph.append(string[strlen])
		strlen-=1;		
				
	return alph;

def filter_alphabets(string , alph):
	result = "";
	for i in range(0,len(string)):
		if(string[i] != alph):
			result = result + string[i];
	return result;
def operation(string, pattern):
	t = "";
	s = string;
	
	
	i=len(s);
	pn = 0;
	while(pn < len(pattern)):
		t=  t+s;
		s = filter_alphabets(s , pattern[pn]);
		pn+=1;
		
	return t;	
def convert_to_str(arr):
	result=  "";
	for i in range(0,  len(arr)):
		result += arr[i];
	return result;
def run1(string):
	path = find_path(string);
	path = path[::-1];
	strlen = len(string);
	for i in range(1,strlen):
		result = operation(string[0:i] , path)
		if(result == string):
			
			print(string[0:i] , convert_to_str(path));
			return 1;
	
	return -1;

def run(string):
	if(run1(string) == -1):
		print(-1);



while(1):
	str1 = input("");
	run(str1);
	
