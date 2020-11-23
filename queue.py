# 20/11/2020, Nicolas Keck, Practice queue stuff

queue = []

queue.append("First")
queue.append("Second")
queue.append("Third")
queue.append("Fourth")

queue.pop(0)
queue.pop(0)

#print(queue)
# queue[0] functions the same as peek() would
#print(queue[0])

# 23/11/2020, Implementing a queue as a static data structure
front = -1
rear = -1
queue = [None for a in range(5)]

def enQueue(i):
    global front
    global rear
    if front == -1:
        front = 0
    if rear < len(queue)-1:
        rear += 1
        queue[rear] = i
    else:
        raise Exception("Queue overflow")

def deQueue():
    global front
    global rear
    if front <= rear:
        front += 1
        return queue[front-1]
    else:
        raise Exception("Queue underflow")

def peekQueue():
    global front
    return queue[front]

for a in range(3):
    enQueue(a)
for a in range(2):
    deQueue()
print(peekQueue())