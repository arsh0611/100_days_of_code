""" Given an array arr[] with N elements, the task
is to find out the longest sub-array which has the
shape of a mountain.
The Longest Peak consists of elements that are
initially in ascending order until a peak element
is reached and beyond the peak element all other
elements of the sub-array are in decreasing order.

Input: arr = [2, 2, 2] 
Output: 0 

    Explanation: 
    No sub-array exists that shows the behaviour
    of a mountain sub-array.


Input: arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] 
Output: 11 


    Explanation: 
    There are two sub-arrays that can be
    as mountain sub-arrays. The first one is from
    index 0 – 2 (3 elements) and next one is from
    index 2 – 12 (11 elements).  As 11 > 2, our
    answer is 11.""""




def LongestPeak(a): 
  # Write your code here
  result=0
  if (a[0]<a[1]):
    ascending=True
  else:
    ascending=False
  count=[0]
  counts=0
  for i in range(0,len(a)):
    if i+1 != len(a):
      if(a[i]==a[i+1]):
        break
    if ascending==False:
      if i+1 != len(a):
        if a[i]<a[i+1]:
          counts=counts+1
          count.append(counts)
          counts=0
          ascending=True
        else:
          counts=counts+1
      else:
        counts= counts+1
        count.append(counts)
        break
      
    if(ascending==True):
      counts=counts+1
      if i+1 != len(a):
        if a[i]>a[i+1]:
          ascending=False
          
          
  result= max(count)
  print(count)
  return result
  
  


if __name__ == "__main__":
  d = [ 1, 3, 1, 4, 5, 6,  
        7, 8, 9, 8, 7, 6, 5 ]
  print(LongestPeak(d)) 
      
