"""
    Given a 2d grid map of '1's (land) and '0's (water), count the
    number of islands. An island is surrounded by water and is formed
    by connecting adjacent lands horizontally or vertically. You may
    assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

def removeOnes(a,b):
  c=[]
  for i in a:
    if i in b:
      continue
    else:
      c.append(i)
  return c
def count_island(input_matrix):
  ones=[]
  island=[]
  
  for i in range(0,len(input_matrix)):
    for j in range(0,len(input_matrix[0])):
      if input_matrix[i][j]=="1":
        temp=[i,j]
        ones.append(temp)
  print(ones)
  connected=[]
  connected.append(ones[0])
  
  for i in ones:
    
    for i in connected:
      if i[0]+1 != len(input_matrix) and [i[0]+1, i[1]] not in connected:
        if [i[0]+1, i[1]] in ones:
          connected.append([i[0]+1,i[1]])
    
      if i[0]-1 != -1 and [i[0]-1, i[1]] not in connected :
        if [i[0]-1, i[1]] in ones:
          connected.append([i[0]+1, i[1]])
      if i[1]+1 != len(input_matrix[0]) and [i[0], i[1]+1] not in connected:
        if [i[0], i[1]+1] in ones:
          connected.append([i[0],i[1]+1])
    ones=removeOnes(ones,connected)
    print("remaining ones",ones)
    island.append(connected)
    connected.clear()
    print("island",island)
    if len(ones)==0:
      break
    connected.append(ones[0])
 
    
  print(connected)
      
  return len(island)
if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
  print(count_island(grid))




