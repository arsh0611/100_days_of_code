"""    Write a  program to find maximum of each column of  2d array 

Sample Input -> Output

max_col([[1, 5, 13], [11], [9, 18]]) → [11, 18, 13] 
max_col([[1, 8, 1], [1,21], [9]]) → [9, 21, 1]

"""
import itertools 

def max_col(test_list):
  l=len(test_list)
  max_list=[]
  answer=[]
  for i in range(0,l):
    for j in range(0,3):
      if(len(test_list[j])>i):
        print("index",j)
        print("index i", i)
        max_list.append(test_list[j][i])
    answer.append(max(max_list))
    max_list.clear()
  return answer
    
    
      
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))




