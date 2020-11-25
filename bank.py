# 25/11/2020, Nicolas Keck, Implementation of a bank token system with a circular queue

# Imports
from random import randint

# Queue class
class circleQueue:
    def __init__(self, length):
        self.front = -1
        self.rear = -1
        self.max = length
        self.queue = [None]*length

    def enQueue(self, i):
        if self.rear + 1 == self.front or (self.front == 0 and self.rear == self.max - 1):
            raise Exception("Queue overflow")
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            elif self.rear == self.max - 1:
                self.rear = 0
            else:
                self.rear += 1
            self.queue[self.rear] = i

    def deQueue(self):
        if self.front == -1:
            raise Exception("Queue underflow")
        else:
            if self.front == self.rear:
                temp = self.front
                self.front = -1
                self.rear = -1
            elif self.front == self.max - 1:
                temp = self.front
                self.front = 0
            else:
                temp = self.front
                self.front += 1
            return self.queue[temp]

    def display(self):
        if self.front == -1:
            return None
        else:
            output = []
            iter = self.front
            match = False
            while (not match and iter < self.max):
                if iter == self.rear:
                    match = True
                output.append(self.queue[iter])
                iter += 1
            iter = 0
            while not match:
                if iter == self.rear:
                    match = True
                output.append(self.queue[iter])
                iter += 1
            return output

    def peek(self):
        return self.queue[self.front]


# Actual implementation of token system
tokens = circleQueue(8)
answer = 0
print('"exit" to exit\n"token" for another customer\n"button" to service a customer\n"show" to display the queue')
while answer != "exit":
    answer = input('Query?: ')
    if answer == "token":
        cors = 0
        while cors != "C" and cors != "S":
            cors = input("Savings or Current account(C or S): ").upper()
        token = cors + "-" + str(randint(1,200))
        tokens.enQueue(token)
        print(f"{token} added to queue")
    elif answer == "button":
        print(f"{tokens.deQueue()} removed from queue")
    elif answer == "show":
        print(tokens.display())
