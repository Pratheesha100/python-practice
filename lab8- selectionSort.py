#implentation of slection sort algorithm

#get keyboad inputs
A=[] #create an empty array

for i in range(5):
    A.append(int(input('Enter a number:')))
print(A)


def selectionSort(A):
    n=len(A)
    for j in range(0,n-1):
        smallest=j
        for i in range(j+1,n):
            if (A[i]<A[smallest]):
                smallest=i
            A[j],A[smallest]=A[smallest],A[j]

selectionSort(A)
print('Sorted array: ',A)
