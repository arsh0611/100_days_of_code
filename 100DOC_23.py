"""Write an efficient algorithm that searches for a value
in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer
    of the previous row.



Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: True


Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: False"""


def find_target(input_matrix,target):
  row=0
  l=len(input_matrix)
  if l==1:
    if(len(input_matrix[0])==0):
      return False
    elif(len(input_matrix[0])==1):
      if(input_matrix[0][0]==target):
        return True
      else:
        return False
      
  
  mid=int(l/2)
  low=0
  Row_len = len(input_matrix[0])
  upper=l-1
  
  
  
  while(low<upper):
    if low+1 == mid:
      if(target> input_matrix[low][Row_len -1]  and target< input_matrix[mid][0]):
        row=-1
        break
    if upper-1 == mid:
      if target> input_matrix[mid][Row_len-1] and target < input_matrix[upper][0]:
        row = -1 
        break
    print("abc")
    
    if(target<input_matrix[0][0] or target> input_matrix[upper][Row_len - 1]):
      row=-1
      break
    
    
    if(target>input_matrix[mid][0] and target< input_matrix[mid][Row_len -1 ]):
      row=mid
      print('found')
      break
    elif(target<input_matrix[mid][0]):
      print('target less than mid')
      upper=mid
    elif target>input_matrix[mid][Row_len-1]:
      print(input_matrix[mid][Row_len-1])
      print('target less than mid')
      low = mid
    mid=int((low+upper)/2)
    
    
  print(row)
  if row==-1:
    return False
  
  matrix = input_matrix[row]
  low = 0
  high = Row_len-1
  
  
  while low <= high: 
  
    mid = low + (high - l) // 2;
    print("LOW ",low)
    print("high ",high)
    print("mid ",mid)
    if matrix[mid] == target: 
      return True 
    elif matrix[mid] < target: 
      low = mid + 1
    else: 
      high = mid - 1
  return False
    
  
  
  
  
    
    
    
if __name__ == "__main__":
  input_matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
  ]
  target = 3
 
  print(find_target(input_matrix,target))
  print("hello")





