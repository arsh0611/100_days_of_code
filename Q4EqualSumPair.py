"""Given an integer array of size N, determine
whether 4 elements exist such that a+b = c+d.
Return true or false accordingly. Perform this
in O(n^2). Note : (a+b) and (c+d) is unique.
For eg, array(10, 10, 8, 9) Pair(10(at index 0),8)
and Pair(10(at index 1),8) are different pairs but
Pair(10(index 0),10(index 1)) and Pair(10(index 1)
,10(index0)) are same."""

n= int(input())
arrays = list(map(int,input().split()))
h=[]
flag = False
for i in range(0,n-1):
  for j in range(i+1, n-1):
    sum= arrays[i]+arrays[j]
    if sum in h:
      flag = True
    else:
      h.append(sum)
  if flag==True:
    break
if flag==True:
  print("true")
else:
  print("false",end ="")
      
      
 
    



