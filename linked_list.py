class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        itr = self.head
        for _ in range(index):
            itr = itr.next
        return itr.data

    def addAtHead(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node = Node(val, prev.next)
            prev.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
