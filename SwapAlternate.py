"""You have been given an array/list of size N. You need to swap
every pair of alternate elements in the array/list. You have
to change the input array itself and print the result"""


flag=True

a=int(input())
for b in range(a):

  n= int(input())
  arrays  = list(map(int,input().split()))
  
  for i in range(0,n):
      if flag==True and n-1>=i+1:
        temp= arrays[i]
        arrays[i]=arrays[i+1]
        arrays[i+1]=temp
        flag = False
      else:
        flag = True
  for a in arrays:
    if a == arrays[n-1]:
      print(a)
    else:
      print(a,end=" ")
  
