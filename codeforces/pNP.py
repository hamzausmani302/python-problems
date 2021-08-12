
#{
# P = N *  P 
#https://codeforces.com/gym/103241/problem/A
#}




statement = input("");
arr = statement.split(" ");
x = int(arr[0]);
y=  int(arr[1]);

count = 0;


for i in range(0, x+1):
	for j in range(0,y+1):
		if(i*j == i):
			count +=1;


print(count);


