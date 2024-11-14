def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


def quicksort(A,p,r):
    if(p<r):
        q= partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

arr=[]
for i in range(5):
    arr.append(int(input('Enter a number: ')))
print('Original Array: ', arr)
quicksort(arr,0,len(arr)-1)
print('Sorted Array: ',arr)
n=len(arr)
num=arr[-1]
num**=3
print('Cube value of last index number: ',num )
tot=0
for a in range(0,n):
    tot= tot+arr[a]
print('Sumation of the total values: ',tot)
