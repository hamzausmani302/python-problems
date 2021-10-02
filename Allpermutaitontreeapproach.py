
def permute(list1):
	result = [];
	
	
	if(len(list1) == 1):
		copy = [];
		for i in range(0,len(list1)):			#implement in C++;
			copy.append(list1[i]);
		print("")
		return [copy];
	for i in range(0,len(list1)):
		popped = list1.pop(0);		#pop fierst element
		perms = permute(list1);				# call recustion with remaingin arreay
		#print(perms);
		if(perms != None):
			#print(perms);
			for perm in perms:
				perm.append(popped);
				#print(perm)			#push the popped elemt back into the array
			result.extend(perms);
		list1.append(popped);
	return result;
	#print(list1);			#print all the sublists formed	
	#print(list1);
	#print(result);
list12 = [1,2,3,4];
x= permute(list12);
print(len(x));									
