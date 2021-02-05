# 2/4/2021 - Using abstract data structures with files
# This specific program imports specific fields from a csv file and then adds them to a
# linked list
import csv


# Classes for nodes and linked list
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
        if self.head is not None:
            self.tail.next = NewNode
        else:
            self.head = NewNode
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


if __name__ == "__main__":
    Llist = LinkedList()
    # No input sanitization yet
    with open("flatfile.csv", newline='', encoding="utf-8") as file:
        print("Column options: Name, Email, Address, City, Country, Postcode, NetWorth, Quote")
        choice = input("Please input what columns you would like to be loaded "
                       "(Separated by commas): ").lower().split(", ")
        reader = csv.reader(file)
        delrows = []
        first = True
        for row in reader:
            if first:
                for a in range(0,len(row)):
                    if row[a].lower() not in choice:
                        delrows.append(a)
                first = False
            else:
                for a in range(len(delrows)-1, -1, -1):
                    del(row[delrows[a]])
                Llist.endAdd(row)
    choice = input("Would you like to print the linked list? (Y/N): ").upper()
    if choice == "Y":
        Llist.printList()