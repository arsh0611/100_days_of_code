"""Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.

    NOTE : The length of the list is divisible by K

Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5


"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
      lis=[]
      a=[]
      rev=None
      head=None
      i=0
      while(l1!=None):
        for i in range(0,key):
          lis.append(l1.val)
          l1=l1.next
        lis.reverse()
        for i in lis:
          
          if rev==None:
          
            ab=ListNode(i,None)
            rev=ab
            head=rev
          else:
            ab=ListNode(i,None)
            rev.next=ab
            rev=rev.next
        
          
        lis.clear()
      return head
      
a1=ListNode(6)
a2=ListNode(5,a1)
a3=ListNode(4,a2)
a4=ListNode(3,a3)
a5=ListNode(2,a4)
a6=ListNode(1,a5)

sol=Solution()
a=sol.swapLinkedLists(a6,2)
print(a.val)




      
        
