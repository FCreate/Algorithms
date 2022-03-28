class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def insertAfter(self, node, value):
        if node == self.tail:
            self.pushBack(value)
        newNode = Node(value)
        newNode.next = node.next
        newNode.prev = node
        node.next = newNode
        newNode.next.prev = newNode

        return newNode

n = int(input())
length = [int(elem) for elem in input().split()]
k = int(input())
l = DoubleLinkedList()
for elem in length:
    l.pushBack(elem)

sum = 0
for i in range(n):
    sum += length[i]**2
print(sum)
tmp = l.head
i = 0
for _ in range(k):
    command, factory = [int(elem) for elem in input().split()]
    #print("i", i)
    #print("factory - 1", factory-1)
    #print("Node prev")
    #print(tmp)
    if factory - 1 >= i:
        while i != (factory - 1):
            tmp = tmp.next
            #print("Increasing i")
            i += 1
    else:
        while i != (factory - 1):
            tmp = tmp.prev
            #print("Decreasing i")
            i -= 1
    #print("Node next")
    #print("i", i)
    #print("factory - 1", factory-1)
    #print(tmp)
    if command == 1:

        #head
        if tmp.prev is None:
            l.head = tmp.next
            l.head.prev = None
            sum -= (l.head.val**2 + tmp.val ** 2)
            l.head.val += tmp.val
            sum += l.head.val**2
            tmp = l.head
            i = 0
            #del tmp
        #tail
        elif tmp.next is None:
            #print("Delete tail")
            l.tail = tmp.prev
            l.tail.next = None
            sum -= (l.tail.val ** 2 + tmp.val ** 2)
            l.tail.val += tmp.val
            sum += l.tail.val**2
            tmp = l.tail
            i -= 1
            #del tmp
        #middle
        else:
            round_part, residual =  divmod(tmp.val, 2)
            big_part, small_part =round_part + residual, round_part
            sum -= (tmp.val**2 + tmp.prev.val**2+tmp.next.val**2)
            tmp.prev.val += small_part
            tmp.next.val += big_part
            sum += (tmp.prev.val**2 + tmp.next.val**2)
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp = tmp.prev
            i -= 1
            #del tmp
        print(sum)
    #split
    else:
        round_part, residual = divmod(tmp.val, 2)
        #div factory to two parts
        big_part, small_part = round_part + residual, round_part
        #decrease sum
        sum -= (tmp.val**2)
        #insert new val
        node = l.insertAfter(tmp, big_part)
        tmp.val = small_part
        sum += big_part**2 + small_part**2
        tmp = node.prev
        #i-=1
        print(sum)