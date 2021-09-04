from stack_list import StackList

_stack_list = StackList()
print(_stack_list.is_empty())
_stack_list.push(10)
_stack_list.push(11)
_stack_list.push(12)
_stack_list.push(13)
_stack_list.view()
_stack_list.pop()
print('peek',_stack_list.peek())
print(_stack_list.is_empty())

for i in iter(_stack_list):
   print(i)