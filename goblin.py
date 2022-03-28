class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, head):
        self.head = None
        self.tail = None
    def Head(self):
        return self.head
    def Tail(self):
        return self.tail
    def Empty(self):
        return self.head is None

    def pushFront(self, value):
        if self.Empty():
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def pushBack(self, value):
        if self.Empty():
            self.pushFront(value)
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def popFront(self):
        oldHead = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        value = oldHead.val
        del oldHead
        return value

    def popBack(self):
        if self.tail.prev:
            return self.popFront()
        oldTail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        value = oldTail.val
        del oldTail
        return value
    def inserAfter(self, node, value):
        if node == self.tail:
            self.pushBack(value)
        newNode = Node(value)
        

