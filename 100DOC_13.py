"""    Function to check if a singly linked
list is a palindrome

    Given a singly linked list of characters,
    write a function that returns True if the
    given list is a palindrome, else False.


Sample input

("r" -> "a" -> "d" -> "a" -> "r" )


Sample output

True
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkPalindrome(self, l1: ListNode):
      strng=l1.val
      while(l1.next):
        strng=strng+l1.next.val
        l1=l1.next
      print(strng)
      i=0
      j=len(strng)-1
      pal=True
      while(i<=int(len(strng)/2)+1):
        print("i",i," j",j)
        if(i==j):
          return True
        else:
          if(strng[i]!=strng[j]):
            return False
        i=i+1
        j=j-1
      return pal
        
      
    
  



    
    
    
    
    
