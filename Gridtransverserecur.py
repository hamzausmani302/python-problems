
#this problem was to transverse a grid of the given i+1 and j+1 dimension and it returns number of ways to reach the 0 , 0 location from the last location
def transverse(i , j , memo={} ):
    key = str(i) + ","+ str(j);
    if( key in memo):
        return memo[key];
    if(i == 0 and j == 0):
        return 1;
    if(i == -1 or j== -1):
        return 0;

    memo[key] =  transverse(i-1 , j) + transverse(i , j-1);
    return memo[key];

print(transverse(1,1))
print(transverse(2,3))