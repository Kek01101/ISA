# 1/11/2021 - Object implementation of a double-linked list

# To do: Remove and inserting functions don't entirely work with the head and tail. Fix
# at some point.


class Node:
    def __init__(self, data=None, last=None):
        self.data = data
        self.next = None
        self.last = last


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def endAdd(self, data, ret=False):
        NewNode = Node(data, self.tail)
        self.tail.next = NewNode
        self.tail = NewNode
        if ret:
            return NewNode

    def startAdd(self, data, ret=False):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        if ret:
            return NewNode

    def insert(self, data, pos):
        NewNode = Node(data)
        NewNode.next = pos.next
        pos.next = NewNode

    def remove(self, node):
        node.last.next = node.next
        node.next.last = node.last

    def printList(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next


Llist = LinkedList()
with open("randata.txt", "r") as file:
    flist = file.readlines()
    for a in range(len(flist)):
        if a == 0:
            Llist.startAdd(flist[a].strip())
            Llist.tail = Llist.head
        else:
            Llist.endAdd(flist[a].strip())
Llist.printList()