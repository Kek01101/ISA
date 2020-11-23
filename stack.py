# 18/11/2020 - Nicolas Keck, Practice stack stuff

stack = []

stack.append("Jack")
stack.append("Queen")
stack.append("King")
stack.append("Ace")

stack.pop()
stack.pop()

#print(stack)
# Stack[-1] functions the same as a .peek() would
#print(stack[-1])


# Sample IB questions

#Question b
"""
stk = [0, 3, 1, 5, 1, 10, 0, 6, 1, 4]
while stk:
    print("Step", stk.pop())
    if stk.pop() == 0:
        print("Left")
    else:
        print("Right")
"""

#Question c
flowers = ["Yarrow", "Primrose", "Lavender", "Day Lily", "Camellia", "Broom", "Aster"]
fruits = ["Pear", "Orange", "Cherry", "Apple"]
while fruits and flowers:
    X = fruits.pop()
    Y = flowers.pop()
    if X < Y:
        X = X
        #print(X)
    else:
        #print(Y)
        Y = Y

#Question d
flowers = ["Yarrow", "Primrose", "Lavender", "Day Lily", "Camellia", "Broom", "Aster"]
fruits = ["Pear", "Orange", "Cherry", "Apple"]
flofru = []
while fruits:
    flofru.append(fruits.pop())
while flowers:
    flofru.append(flowers.pop())
#print(flofru)

# 23/11/2020, Impementing a stack as a static data structure
top = -1
testStack = [None for a in range(5)]

def stackPush(i):
    global top
    if top < len(testStack)-1:
        top += 1
        testStack[top] = i
    else:
        raise Exception("Stackoverflow")

def stackPop():
    global top
    if top >= 0:
        top -= 1
        return testStack[top+1]
    else:
        raise Exception("Stackunderflow")

def stackPeek():
    return testStack[-1]

for a in range(4):
    stackPush(1)
stackPush(2)
print(stackPeek())