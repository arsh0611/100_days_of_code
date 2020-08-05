"""Print the following pattern for the given number
of rows. Pattern for N = 4 The dots represent spaces.
"""

n= int(input())
for i in range(0,n):
 
  for j in range(0, (n*2-1)-(i*2+1) ):
    print(" ",end="")
  temp=i+1
  for k in range((n*2-1)-(i*2+1)-1, (n*2 -1) -1):
    
    if(k< (     (n*2-1)-(i*2+1)-1+(n*2 -1)    ) /2 ):
      print(temp,end="")
      temp=temp+1
    else:
      temp=temp-1
      print(temp-1,end="")
      
  print(end="\n")
    
    
    
  
