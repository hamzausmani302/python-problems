#google challenge foobar


data = ["" , "abc" , "def" , "ghi" , "jkl"  , "mno" , "pqrs" , "tuv" , "wxyz" , ""];

input1 = "3662277";
words = ["foo" , "bar" , "baz" , "foobar" , "emo" , "cap" , "car" , "cat"  ];
indexes=[];
codes = [];
results = []

def  get_num_for_letter(letter):
	i = 0;
	
	for reg in data:
		for l in reg:
			
			if(l == letter):
				
				return i+1; 
		i = i +1;
	return -1;
def convert_word_to_code(word):
	code = "";
	for letter in word:
		code = code + str(get_num_for_letter(letter));
	return code;


def form_arr():
	
	for word in words:
		codes.append(convert_word_to_code(word));
def get_string(code):
	i = 0;
	for x in codes:
		if(x == code):
			return words[i],  i;
		i = i +1;
def check_words():
	i = 0;
	for code in codes:
		if(code in input1 ):
			word , index = get_string(code);
			results.append(words[i]);
			#results.append(get_string(code));
		i = i +1;
def check_bigger(now ,next1):
	smaller = len(now);
	if(len(next1) < smaller):
		smaller = len(next1);
	for i in range(0 , smaller):
		if(now[i] <  next1[i]):
			return 2;
		elif(now[i] > next1[i]):
			return 1; 
	
	if(len(now) > len(next1)):
		return 1;	
	if(len(next1) > len(now)):
		return 2;
	return 0;		
	
def sort(arr):
	i = 0;
	for j in range(0 , len(arr)-1):
		for i in range(0,len(arr)-1):
		
			if(check_bigger(arr[i] ,arr[i+1]) == 1):
				temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
	return results;		
form_arr();
print(codes);
check_words();
print(sort(results));

