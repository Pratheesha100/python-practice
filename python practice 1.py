char = input('Enter a character:')
print(ord(char))

num=float(input("Enter a number:"))
print(chr(num))

print("A"+'7'+'V')
s=[1,2,3,4,5,6,7,8]

print(s[-3])
print(s[:])
print(s[2:5])
print(s[::-1])

range(1,9)
for i in range(10):
  print(i)
for i in range(10):
  print(i, end=',')

num1 = input('Enter number 1:')
num2 = input('Enter number 2:')
num3 = input('Enter number 3:')
min=num1
if(min>num2):
    min=num2
if(min>num3):
     min=num3
print("Minimum values is "+ min)

#N=1
#if N<=100:
#    if N%5==0:
#        print(N)
#    else:
#        N+=1
#else:
#  print('Done')



