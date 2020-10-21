from zadanie1 import LinkedList, Node

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __repr__(self):
        s=""
        node = self.queue.head
        while node:
            s += node.value + ", "
            node = node.next
        return s[:-2]

    def peek(self):
        return self.queue.node(0)

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop()

    def __print__(self):
        return self.__repr__

    def __len__(self):
        return len(self.queue)


queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
