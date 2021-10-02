
# backtracking to find the all the possible combinatiions that lead to a target sum

def target_sum(array , arr,result, sum1 ,   tsum):
	
	if(sum1 == tsum):
		result.append(arr);
		return result;	#change
	elif(sum1 < tsum):
		
		for i in range(0,len(array)):
			if(sum1 + array[i] <= tsum):
				arr.append(array[i]);
				res = target_sum(array , sum1+array[i] , tsum  );
				#arr.pop();
				print(res);
	return result;	

a = [];
re = [];
target_sum([1,2,3],a,re , 0 , 5);
