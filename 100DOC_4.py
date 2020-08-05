"""Four Number Sum

Write a function that takes in a non-empty array
of distinct integers and an integer representing
a target sum.
The function should find all quadruplets in the
array that sum up to the largest sum and return
a two dimensional array of all these quadruplets
in no particular order.

This is the last of its kind, I hope you would
have understood the concept of storing complements
in the set / dictionary or after sorting the list
we can use two pointers to decide whether to decrement
/ increment the pointers. This problem also works on
the similar principle, so don't get trapped into the
4 loop Naive Solution.

Sample Input

array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output
// the quadruplets could be ordered differently
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optimal Space & Time Complexity

Average: O(n^2) time | O(n^2) space - where n is the
length of the input arrayTwo
Worst: O(n^3) time | O(n^2) space - where n is the
length of the input array

"""

def fourNumberSum(array, targetSum):
  
  a=[0]*1000
  b=[] 
  for i in array:
      a[i]=1
  for j in array:
      for k in array:
        for l in array:
          if j==k or targetSum-j-k-l == j or targetSum-j-k-l == k or targetSum-j-k-l == l or k==l or j==l:
            print("",end="")
        
          elif a[targetSum-(j+k+l)]==1:
      
            e=[targetSum-j-k-l, j, k,l]
            
          
            b.append(e)
          
         
        
  res=[]
  for i in b:
    i.sort()
    if i not in res:
      
      res.append(i) 
                    

  return res
  
  
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
