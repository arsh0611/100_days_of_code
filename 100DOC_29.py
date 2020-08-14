"""Instructions from your teacher:

    Given a matrix of M x N elements (M rows, N columns),
    return all elements of the matrix in diagonal order as
    shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""
def return_diag(input_matrix):
  number_of_elements = len(input_matrix)*len(input_matrix[0])
  print("n", number_of_elements)
  i,j=0,0
  answer=[]
  increasing = True
  
  while(number_of_elements>0):
    print("I ", i)
    print("j ",j)
    
    if (i==0 and j==0) or (i==len(input_matrix)-1 and j==len(input_matrix[0])-1):
      print("1:")
      answer.append(input_matrix[i][j])
      j=j+1
      increasing=False
    elif increasing==False and i+1 != len(input_matrix) and j-1 != -1:
      print("2:")
      answer.append(input_matrix[i][j])
      i=i+1
      j=j-1
    elif increasing == False and j-1 == -1 and i+1 != len(input_matrix):
      
      print("3:")
      answer.append(input_matrix[i][j])
      i=i+1
      increasing=True
    elif increasing == False and j-1 == -1 and i+1 == len(input_matrix):
      print("8:")
      answer.append(input_matrix[i][j])
      j=j+1
      increasing= True
      
    elif increasing==True and i-1 != -1 and j+1 != len(input_matrix[0]):
      print("4:")
      answer.append(input_matrix[i][j])
      i=i-1
      j=j+1
    elif increasing==True and i-1==-1 and j+1 == len(input_matrix[0]):
      print("5:")
      answer.append(input_matrix[i][j])
      i=i+1
      increasing=False
    elif increasing==True and i-1==-1 and j+1 !=len(input_matrix[0]):
      print("6:")
      answer.append(input_matrix[i][j])
      j=j+1
      increasing=False
    elif increasing==False and i+1==len(input_matrix):
      print("7:")
      increasing=True
      answer.append(input_matrix[i][j])
      j=j+1
    elif increasing == True and j+1 ==len(input_matrix[0]):
      print("9:")
      answer.append(input_matrix[i][j])
      i=i+1
      increasing=False
      
      
    
    
    
    number_of_elements= number_of_elements-1
    print("answer : ",answer)
    print("")
  
  
  

      
    
  #write your code here
  return answer
if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  input_matrix =  [
     [ 1, 2, 3, 4, 5 ],
     [ 6, 7, 8, 9, 10 ],
     [ 11, 12, 13,14, 15 ],
     [ 16, 17, 18,19, 20 ]
    ]
  print(return_diag(input_matrix))




