#zadanie1 - Beata Ostrowska
from typing import Any

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ""
        repr = self.head
        while repr:
            s += str(repr.value) + " -> "
            repr = repr.next
        return s[:-4]

    def push(self, value):
        el = Node(value)
        el.next = self.head
        if self.tail == None:
            self.tail = el
        self.head = el

    def append(self,value):
        el = Node(value)
        if self.head == None:
            self.head = el
            self.tail = el
        else:
            self.tail.next = el
            self.tail = el
        
            
    def node(self, value):
        a = .len
        print(a)
        #if a < value:
         #   return "Error"
        poz = value
        el = self.head
        while poz:
            el = el.next
            poz -= 1
        return  el.value
    #insert
    #pop
    #remove_last
    #remove
    #print
    def len(self):
        v= 0
        node = self.head
        while node:
            v += 1
            node = node.next
        return v


list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(1)
print(middle_node)
# list_.insert(5, after=middle_node)

# assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

# first_element = list_.node(at=0)
# returned_first_element = list_.pop()

# assert first_element.value == returned_first_element

# last_element = list_.node(at=3)
# returned_last_element = list_.remove_last()

# assert last_element.value == returned_last_element
# assert str(list_) == '1 -> 5 -> 9'

# second_node = list_.node(at=1)
# list_.remove(second_node)

# assert str(list_) == '1 -> 5'
