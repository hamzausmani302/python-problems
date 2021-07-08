
arr1= [3,3,4,3,4,1234,13,12,31,23,213,21,3,21];
def sum1(arr):
    s = 0;
    for i in arr:
        s += i;
    return s;
def sort(arr):
    for i in range(0 , len(arr)):
        for j in range(0 , len(arr)-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1]= temp;
    return arr;
def rev(arr):
    i=0;
    j = len(arr)-1;
    while(i < j):
        temp =arr[i];
        arr[i]= arr[j];
        arr[j] = temp;
        i +=1;
        j -=1;
    return arr;

def divide_and_conquer(tsum ,arr,i , j , memo={}):

    if(i >= j):
        return False;
    middle= int(j-1);

    s = 0;
    ind = i;
    query = str(i) + "," + str(j);

    if(query in memo):
        print(query +"="+ str(memo[query]));
        s = memo[query];
    else:

        while(ind < j):
            s += arr[ind];
            ind +=1;
        print("i =" + str(i) + " j = " + str(j) + "  middle= " + str(middle) + " sum = " + str(s));
        memo[query] = s;

    if(s == tsum):
        return True;
    return divide_and_conquer(tsum , arr,i, middle,memo);
    return divide_and_conquer(tsum ,arr,middle+1, j , memo);


def find(arr , num):
   x= divide_and_conquer(num, arr, 0, len(arr) , {});
   y= divide_and_conquer(num, rev(arr), 0, len(arr) , {});
   if(x == True or y == True):
       return True;
   return False;

arr1 = sort(arr1);
print(find(arr1, 9));



