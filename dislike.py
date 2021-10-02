


def opposite(w , wd , tofind):
	if(wd-w == 1 or wd-w == -1 ):
		return -1;
	
	
	
	totalnumbers = abs((wd-w)*2);  
	diff = abs(wd-w);
	if(w > totalnumbers ):
		return -1;
	if(tofind > totalnumbers or wd> totalnumbers):
		return -1;
	res=0 ;
	max1 = max(w,wd);
	if(tofind >= totalnumbers/2+1):
		
		res = tofind - diff;
	else:
		res= tofind+diff;
	
	if(res > totalnumbers or res <=0 ):
		return -1;
	
	return res;





	
repeat = int(input(""));
	
for i in range(0, repeat):
	line = input("");
	arr= line.split(" ");
			
	print(opposite(int(arr[0]),int(arr[1]),int(arr[2])) );
		
		
		
	
	
