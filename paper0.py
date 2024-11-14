def multiply(M,n):
    if(n==1):
        return M
    else:
        return (M + multiply(M,n-1))

while(True):
    
      M = int(input('Enter a number for M: '))
      if(M==-1):
          break
      n = int(input('Enter a number for n: '))

      value=str(multiply(M,n))
      print("Multiply value of:"+value)
      #print("Multiplication of",M,"&",n,"is = ", multiply(M, n)) 

