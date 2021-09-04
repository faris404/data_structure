

class Queue:

   def __init__(self,max=10):
      self.queue = []
      self.max = max
      self.rear = -1


   def enqueue(self,data):
      if self.rear == self.max - 1:
         raise Exception("Queue is full")
     
      self.queue.append(data)
      self.rear += 1
      return self.rear

   def dequeue(self):
      if self.rear == self.max -1:
         raise Exception("Queue is empty")
      self.rear -= 1
      return self.queue.pop(0)

   def isEmpty(self):
      return self.queue == []

   def isFull(self):
      return self.rear == self.max - 1

   def peek(self):
      return self.queue[0]