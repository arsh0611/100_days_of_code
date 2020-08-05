 """   Monotonic Array

    Write a function that takes in an array of integers
    and returns a boolean representing whether the array
    is monotonic.

    An array is said to be monotonic if its elements,
    from left to right, are entirely non-increasing or
    entirely non -decreasing.


SSample Input:

aSample Output:

TTrue

    Time Complexity:  O(n) time | O(1) space, where n,
    is the length of the array
    """
def assending(array):
  for i in range(0,len(array)):
    if i!=len(array)-1:
      if(array[i]<=array[i+1]):
        continue
      else:
        return False
  return True
        

def descending(array):
    for i in range(0,len(array)):
        if i!=len(array)-1:
            if(array[i]>=array[i+1]):
                continue
            else:
               
                return False
    return True
  
def monoArray(array):
    
    if array[0]>array[1]:
  
        return descending(array)
    else:

        return assending(array)
  
  
    
    


if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
  print(monoArray(array))
