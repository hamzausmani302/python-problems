


def get_c(arr , n):
	
	numer = arr[1] - arr[0];
	return numer;

def get_m_approx(arr , n):
	c = get_c(arr,n);
	if(c<0):
		print(-1);
		return -1;
	elif(c ==0):
		
		print(0);
		return 0;	
	nums = [];
	for i in range(1, n-1):
		
		if(arr[i] == 0 and i != 0):
			prev= arr[i-1];
			print(c+arr[i-1] , c);
			return c+arr[i-1];
		prev = arr[i-1];
		if(c+prev != arr[i]):
			
			num = (c+prev)-arr[i];
			nums.append(num);
			print(num , c);
			return num;
	print(-1);		
	return -1;
	
n = int(input(""));
for i in range(0,n):
	n1 = int(input(""));
	data = input("").split(' ');
	tosend = [];
	for j in range(0,n1):
		tosend.append(int(data[j]));
	res = get_m_approx(tosend , n1);
	
