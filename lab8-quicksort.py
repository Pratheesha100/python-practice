A=[]
for i in range(5):
    A.append(int(input('Enter a number: ')))
    print(A)

def partition(A,p,r):
    x=A[r]
    i=(p-1)
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quickSort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

quickSort(A,0,len(A)-1)
print('Sorted Array: ')
print(A)
