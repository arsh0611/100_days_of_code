"""   You are given two non-empty linked lists
representing two non-negative integers. The most
significant digit comes first and each of their
nodes contain a single digit. Add the two numbers
and return it as a linked list.

    You may assume the two numbers do not contain
    any leading zero, except the number 0 itself.

Sample input

(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)


Sample output

7 -> 8 -> 0 -> 7 """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      val,val2=[],[]
      val.append(l1.val)
      val2.append(l2.val)
      
      #creating list from linked list 1 
      while(l1.next):
        val.append(l1.next.val)
        l1=l1.next
      #creating list from linked list 2
      while(l2.next):
        val2.append(l2.next.val)
        l2=l2.next
      if(len(val)>len(val2)):
        sumArray=self.sumofarray(val,val2,len(val),len(val2))
      else:
        sumArray=self.sumofarray(val2,val,len(val2),len(val))
        
      #creating Linked List from array
      node=ListNode(sumArray[len(sumArray)-1])
      
      for i in range(len(sumArray)-2, -1, -1):
        node2=ListNode(sumArray[i],node)
        node=node2
      if(len(sumArray)==1):
          return node
      return(node2)
        
    #method to find sum from two lists   
    def sumofarray(self,a,b,n,m):
      sum=[]
      i=n-1
      j=m-1
      c=0
      s=0
      while j>=0:
        s=a[i]+b[j] +c
        sum.append(int(s%10))
        c=int(s/10)
        i=i-1
        j=j-1
      while i>=0:
        s=a[i]+c
        sum.append(int(s%10))
        c=int(s/10)
        i=i-1
      if c!=0:
        sum.append(c)
      sum.reverse()
      return sum
        
      
      
        

