"""    Given two strings s and t , write a function to determine
if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: True

Example 2:

Input: s = "rat", t = "car"
Output: False
"""



def check_anagram(sentence_1,sentence_2):
  sentence_1=sentence_1.replace(" ","")
  sentence_1=sentence_1.lower()
  sentence_2=sentence_2.replace(" ","")
  sentence_2=sentence_2.lower()

  for i in sentence_1:
    if i in sentence_2:
  
      sentence_1=sentence_1.replace(i," ",1)
      sentence_1=sentence_1.lower()
      sentence_2=sentence_2.replace(i," ",1)
      sentence_2=sentence_2.lower()
     
  
  if sentence_1== sentence_2:
    return True
  else:
    return False
  #write your code here
  return res
if __name__ == "__main__":
  sentence_1 = "anagram"
  sentence_2 = "nagaram"
  print(check_anagram(sentence_1,sentence_2))







