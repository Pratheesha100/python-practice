array=[]
for i in range(5):
    array.append(int(input('Enter a number: ')))
print('Original array: ')
print(array)

def bubbleSort(A):
    n=len(A)
    for i in range(1,(n-1)):
        for j in range(1,n-i+1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]

bubbleSort(array)
print('Sorted array: ')
print(array)
    
