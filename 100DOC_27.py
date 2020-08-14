"""
    Given a string s. Return all the words vertically in the same
    order in which they appear in s.
    Words are returned as a list of strings, complete with spaces
    when is necessary. (Trailing spaces are not allowed).
    Each word would be put on only one column and that in one column
    there will be only one word.

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
"""
"""converting string to list of words"""
def StringToList(input_string):
  word_list=[]
  word=""
  
  for i in range(0,len(input_string)):
    if input_string[i]==" ":
      word_list.append(word)
      word=""
    elif i==len(input_string)-1:
      word=word+input_string[i]
      word_list.append(word)
      word=""
    else:
      word=word+input_string[i]
  return word_list

"""find length of longest word"""
def LongestWord(word_list):
  length=0
  for i in word_list:
    temp=len(i)
    if temp>length:
      length=temp
  return length
      
  
  
"""converting list to word to vertical list"""
def return_vertically(input_string):
  word_list=StringToList(input_string)
  longest_word = LongestWord(word_list)
  print(longest_word)
  print(word_list)
  vertical_list=[]
  
  """initializing empty list"""
  for i in range(0,longest_word):
    vertical_list.append("")
  
  
    
  for word in word_list:
    for i in range(0,longest_word):
      if i<len(word):
        vertical_list[i]=vertical_list[i]+word[i]
      else:
        vertical_list[i]=vertical_list[i]+" "
        
  """deleting trailing spaces"""
  for i in range(0, len(vertical_list)):
    vertical_list[i]=vertical_list[i].rstrip()
    
  
  return vertical_list
  
  
      
      
    
  
  
      
    
    
if __name__ == "__main__":
  input_string = "TO BE OR NOT TO BE"
  
  print(return_vertically(input_string))






