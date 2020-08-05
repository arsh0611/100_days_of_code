"""Print the following pattern Pattern for N = 4 1 23 345 4567 """

n= int(input())

for i in range(1,n+1):
  temp=i
  for j in range(1, n-i+1):
    print(" ",end="")

  for k in range(n-i, n):
    print(temp,end="")
    temp=temp+1
  print()
