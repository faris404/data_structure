from linkedlist import LinkedList


_list = LinkedList()

_list.middle(1,0)
_list.last(2)
_list.last(3)
_list.last(5)
_list.first(0)
_list.middle(4,4)
_list.middle(6,6)
_list.view()
_list.rfirst()
_list.rlast()
_list.view()
_list.rmiddle(3)
_list.view()

for i in iter(_list):
   if (i.data==2):
      i.data=12
_list.view()

print('===== reverse list =======')
evens = LinkedList()
evens.last(2)
evens.last(4)
evens.last(6)
evens.last(8)
evens.last(10)
evens.view()
evens.reverse()
evens.view()
