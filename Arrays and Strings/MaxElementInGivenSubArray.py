def solv(arr,k):
    result=[]
    for i in range(len(arr)-k+1):
        result.append(max(arr[i:i+k]))
    
    return result

# test the function
arr=[1,3,-1,-3,5,3,6,7]
k=3

print(solv(arr,k))