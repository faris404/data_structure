
class Node:
   def __init__(self,data):
      self.data = data
      self.next = None


class StackList:

   def __init__(self):
      self.head = None
      self.tos = -1

   def push(self,data):
      if self.head:
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node
         self.tos += 1
         return data
      self.head = Node(data)
      self.tos += 1
      return data

   def pop(self):
      if self.head:
         data = self.head.data
         self.head = self.head.next
         self.tos -= 1
         return data
      raise Exception('Stack Uderflow')


   def peek(self):
      if self.tos == -1:
         raise Exception("Stack is Empty")
      return self.head.data


   def is_empty(self):
      return self.tos == -1


   def __iter__(self):
      self._iter = self.head
      return self

   def __next__(self):
      if not self._iter:
         raise StopIteration
      data = self._iter.data
      self._iter = self._iter.next
      return data

         
   def view(self):
      current_node = self.head
      while current_node:
         print(current_node.data,end=" -> ")
         current_node = current_node.next
      print(None)
