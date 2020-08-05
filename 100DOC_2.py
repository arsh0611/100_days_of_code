"""    Write a function that takes in a non empty array
of distinct integers and an integer representing a target
sum. 
    The function should find a list of triplets in the
    array that sum upto the target sum and return a
    two-dimensional array of all the these triplets.
    The numbers in each triplet should be order in
    ascending order, and the triplets themselves should
    be ordered in ascending order with respect to the
    numbers they hold.

    If no three numbers sum up to the target sum, the
    function should return an empty array.


Sample Input:

array = [12, 2,1, 3, -6, 5, -8, 6]
targetSum = 0


Sample Output:

[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""


def threeNumberSum(array, targetSum):
    a=[0]*1000
    b=[] 
    for i in array:
        a[i]=1
    for j in array:
        for k in array:
            
            if j==k or targetSum-j-k == j or targetSum-j-k == k:
              print("",end="")
        
            elif a[targetSum-(j+k)]==1:
                e=[targetSum-j-k, j, k]
                
                b.append(e)
    res=[]
    for i in b: 
      i.sort()
      if i not in res: 
        res.append(i) 
                    
    res.sort()
    return res
  
    
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  print(threeNumberSum(array, targetSum))
  
