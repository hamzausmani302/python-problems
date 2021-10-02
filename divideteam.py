
#divide player into two teams with nlog2n comlexity

def merge(arr,  l,  mid, h ):
	nleft = mid-  l+1;
	nright = h - mid ;
	L = arr[l:l+nleft];
	R = arr[mid+1 : mid+1 + nright];
	
	lcursor = 0;
	rcursor = 0;
	k = l;
	
	while(lcursor < nleft and rcursor < nright):
		#print(L[lcursor] ,R[rcursor] , lcursor , rcursor )
		if(L[lcursor] <= R[rcursor]):
			arr[k] = L[lcursor];
			lcursor+=1;
		else:
			arr[k] = R[rcursor];
			rcursor+=1;	 
		k+=1;
	
	while(lcursor < nleft):
		arr[k] = L[lcursor];
		lcursor+=1;
		k+=1;
	while(rcursor < nright):
		arr[k] = R[rcursor];
		rcursor+=1;
		k+=1;
	
	print(L,R,arr);
	return arr;
def mergesort(arr , l ,h):
	
	if(l < h):
		print(arr[l:h]);
		mid = l + int((h-l)/2);
		mergesort(arr , l , mid );
		mergesort(arr, mid+1 , h);
		merge(arr , l , mid , h);
		
		
	
	

def divide(players  ):
	mergesort(players , 0 , len(players)-1);
	a = [];
	sum_a = 0;
	sum_b = 0;
	b = [];
	copy = players[0:len(players)];
	
	while(len(copy)>0):
		el = copy.pop(0);
		if(sum_a > sum_b):
			b.append(el);
			sum_b += el;
		elif(sum_b >= sum_a):
			a.append(el);
			sum_a += el;	
	return 	a,b;
	
	
	
	pass;

players = [1,2,3,4,5,6,7,8,9,10];  #1 1 1 1 2 3 9 10
a,b = divide(players);
print(a,b);


