
arr1= [111,222,3,42213,521321,74,83,9,101];
def sum1(arr):
    s = 0;
    for i in arr:
        s += i;
    return s;
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

def divide_and_conquer(tsum ,arr,i , j):
    if(i >= j):
        return False;
    middle= int(j-1);

    s = 0;
    ind = i;
    while(ind < j):
        s += arr[ind];
        ind +=1;
    print("i =" + str(i) + " j = " + str(j) + "  middle= " + str(middle) + " sum = " + str(s));
    if(s == tsum):
        return True;
    return divide_and_conquer(tsum , arr,i, middle);
    return divide_and_conquer(tsum ,arr,middle+1, j);


def find(arr , num):
   x= divide_and_conquer(num, arr, 0, len(arr));
   rev(arr1);
   y=divide_and_conquer(num, arr, 0, len(arr));
   if(x == True or y == True):
       return True;
   return False;


print(find(arr1, 267));



