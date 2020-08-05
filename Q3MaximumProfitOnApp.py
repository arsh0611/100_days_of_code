"""You have made a smartphone app and want to set
its price such that the profit earned is maximised.
There are certain buyers who will buy your app only
if their budget is greater than or equal to your
price. You will be provided with a list of size N
having budgets of buyers and you need to return the
maximum profit that you can earn. Lets say you decide
that price of your app is Rs. x and there are N
number of buyers. So maximum profit you can earn
is : m * x where m is total number of buyers whose
budget is greater than or equal to x."""

def mP(arr):
  cost = 0
  profit = 0
  number = 1
  pr=[]
 
  while number != 0:
    number  = 0 
    for i in range(0, len(arr)):
      if cost<= arr[i]:
        number = number+1
    temp = number*cost
    
    
    pr.append(temp)
    
    
    cost = cost +1
  pr.sort()
  
  return(pr[len(pr)-1])


n = int(input())
arr = [int(ele) for ele in input().split()]
ans = mP(arr)
print(ans,end="")
