A=[]
for i in range(10,20):
    A.append(input("Enter a number: "))
print("Original Array:",A)

def insertsort(A):
    count=0
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while(i>0 and A[i]>key):
            count+=1
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    print(f'The while loop executed {count} times.')
        
insertsort(A)
print('Sorted Array')
for a in range(len(A)):
    print(A[a],end=' ')

