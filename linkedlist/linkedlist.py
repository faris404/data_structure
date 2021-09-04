
class Node:
   def __init__(self,data):
      self.data = data
      self.next = None


class LinkedList:

   def __init__(self) -> None:
      self.head = None
  
  
   def first(self,data):
      if self.head:
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node
         return data
      self.head = Node(data)
      return data

   def middle(self,data,pos):
      if pos < 1 or self.head==None:
         self.first(data)
         return data


      current_node = self.head
      current_pos = 0

      while current_node.next:
         
         current_pos += 1
         if pos == current_pos:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            return data
         current_node=current_node.next
      return self.last(data)
      
   
   def last(self,data):
      if self.head:
         current_node = self.head
         while current_node.next:
            current_node = current_node.next
         current_node.next = Node(data)
         return data
      self.head = Node(data)
      return data


   def rfirst(self):
      if self.head:
         data = self.head.data
         self.head = self.head.next
         return data
      raise Exception('List is Empty')


   def rmiddle(self,pos):
      if not self.head:
         raise Exception('List is Empty')
      if pos < 1:
         self.rfirst()
      current_node = self.head
      current_pos = 0
      while current_node.next:
         current_pos += 1
         if pos == current_pos:
            data = current_node.next.next.data
            current_node.next = current_node.next.next
            return data
         current_node = current_node.next
      self.rlast()


   def rlast(self):
      if self.head == None:
         raise Exception('List is Empty')
      
      current_node = self.head
      while current_node.next:
         if current_node.next.next == None:
            data = current_node.next.data
            current_node.next = None
            return data
         current_node = current_node.next




   def __iter__(self):
      self._iter = self.head
      return self

   def __next__(self):
      if not self._iter:
         raise StopIteration
      data = self._iter
      self._iter = self._iter.next
      return data
      
   def view(self):
      current_node = self.head
      while current_node:
         print(current_node.data,end=" -> ")
         current_node = current_node.next
      print(None)
