"""Given a linked list, remove the n-th node
from the end of the list and return its head.
Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end,
the linked list becomes 1->2->3->5.

Note:
Given n will always be valid."""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      
      head_new=head
      temp=head

      count=0
      
      while(head.next):
        count=count+1
        head=head.next

      head=head_new
      n=count+1-n
      
      val=False
      if count==n:
        val=True
      i=0
      while(i<=n+1):
        if i==n:
          if val==True:
            temp.next=None
            break
          elif n==0:
            head_new=head.next
          else:
            temp.next=head.next
        temp=head
        head=head.next
        i=i+1
      return head_new
      



        

    
    


    
    
    
    
    
