"""    Write a Python program to search a
specific item in a singly linked list and
return true if the item is found otherwise
return false.

Sample input

items = singly_linked_list()

items.append_item('PHP')

items.append_item('Python')

items.append_item('C#')

items.append_item('C++')

items.append_item('Java')

items.search_item('SQL')


Sample output

False"""


class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, data):
      node = Node(data)
      if self.head:
        self.head.next = node
        self.head = node
      else:
        self.tail = node
        self.head = node
      self.count += 1
    def search_item(self, val1):
      current_item=self.tail
      while current_item:
        val = current_item.data
        current_item = current_item.next
        if val == val1:
          return True
      return False
        

if __name__ == "__main__":
  items = singly_linked_list()
  items.append_item('PHP')
  items.append_item('Python')
  items.append_item('C#')
  items.append_item('C++')
  items.append_item('Java')
  
  print(items.search_item('SQL'))
