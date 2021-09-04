from queue_list import QueueList


odd_numbers = QueueList()
print(odd_numbers.is_empty())
odd_numbers.enqueue(1)
odd_numbers.enqueue(3)
odd_numbers.enqueue(5)
odd_numbers.view()
odd_numbers.dequeue()
odd_numbers.view()
print(odd_numbers.peek())
print(odd_numbers.is_empty())