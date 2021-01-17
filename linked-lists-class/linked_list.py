# 1/11/2021 - Object implementation of a double-linked list
import csv
# Updated 1/17/2021: Switched to CSV data set and improved functionality
# To Do: Add comments explaining function purposes


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
        if self.head is not None:
            self.head.last = NewNode
        self.head = NewNode
        if ret:
            return NewNode

    def insert(self, data, pos, ret=False):
        NewNode = Node(data)
        NewNode.next = pos.next
        pos.next = NewNode
        if ret:
            return NewNode

    def remove(self, node):
        if node == self.head:
            node.next.last = None
        elif node == self.tail:
            node.last.next = None
        else:
            node.last.next = node.next
            node.next.last = node.last

    def printList(self, count=False):
        node = self.head
        if count:
            counter = 0
            out = "Current list state:\n"
            while node is not None:
                out += f"{counter}: {node.data}; "
                counter += 1
                node = node.next
            print(out)
        else:
            while node is not None:
                print(node.data)
                node = node.next

    def search(self, data):
        node = self.head
        while node.data != data and node.next is not None:
            node = node.next
        if node.next is not None:
            return node


Llist = LinkedList()
pointers = []
with open("randata.csv", newline='') as file:
    reader = csv.reader(file)
    flist = []
    for row in reader:
        flist.append(row)
    for a in range(len(flist)):
        if a == 1:
            node = Llist.startAdd(flist[a], True)
            Llist.tail = Llist.head
            pointers.append(node)
        elif a != 0:
            b = False
            while not b:
                choice = input(f"New data: {flist[a]}\nWhat would you like to do with this data?\n1. "
                               f"Insert into list\n2. Add to end of list\n3. Add to start of list\n")
                if choice == '1':
                    Llist.printList(True)
                    while not b:
                        choice = int(input("After what node number would you like to input the data?\n"))
                        if choice <= len(pointers)-1:
                            node = Llist.insert(flist[a], pointers[choice], True)
                            pointers.append(node)
                            b = True
                elif choice == '2':
                    node = Llist.endAdd(flist[a], True)
                    pointers.append(node)
                    b = True
                elif choice == '3':
                    node = Llist.startAdd(flist[a], True)
                    pointers.append(node)
                    b = True
Llist.printList()