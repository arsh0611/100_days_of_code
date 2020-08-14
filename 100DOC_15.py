"""    Merge two sorted linked lists and return
it as a new list. The new list should be made by
splicing together the nodes of the first two lists,
and should also be sorted.

For example, given the following linked lists :

5 -> 8 -> 20 
4 -> 11 -> 15

The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      newListHead=None
      newList=None
      if(l1.val<l2.val):
        newListHead=l1
        newList=newListHead
        l1=l1.next
      else:
        newListHead=l2
        newList=newListHead
        l2=l2.next
        
      while(l1!=None or l2!=None):
        if l1==None:
          newList.next=l2
          newList= newList.next
          l2=l2.next
          
        elif l2==None:
          newList.next=l1
          newList= newList.next
          l1=l1.next
        
        else:
          if(l1.val < l2.val):
            newList.next=l1
            newList=newList.next
            l1=l1.next
          else:
            newList.next=l2
            newList=newList.next
            l2=l2.next
          
      return newListHead
      
