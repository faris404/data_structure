from queue import Queue

names = Queue()

print("is empty",names.isEmpty())
print('is full',names.isFull())

print('push',names.enqueue('hello'))
print('push',names.enqueue('world'))
print('push',names.enqueue('coding'))

print('pop',names.dequeue())
print('pop',names.dequeue())
print('pop',names.dequeue())
print('pop',names.dequeue())

print('peek',names.peek())
print('pop',names.dequeue())
print('is empty',names.isEmpty())
print('is full',names.isFull())