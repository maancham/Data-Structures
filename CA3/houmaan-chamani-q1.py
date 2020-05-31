class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         if(len(self.items) == 0):
             return 0
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

myStack = Stack()
indexex = Stack()
n = int(input())
seeFront = []
seeBack = []
for i in range(0, n):
    seeFront.append(0)
    seeBack.append(0)
towers = list(int(i) for i in input().split())
myStack.push(towers[0])
indexex.push(0)
for i in range(0,len(towers)):
    if myStack.isEmpty() == True:
        myStack.push(towers[i])
        indexex.push(i)
        continue
    if(myStack.isEmpty() == False):
        while(True):
            if((myStack.isEmpty() == True) or (myStack.peek() >= towers[i])):
                break
            tmpI = indexex.pop()
            myStack.pop()
            print("set front ", tmpI, "__", i - tmpI)
            seeFront[tmpI] = i - tmpI
        myStack.push(towers[i])
        indexex.push(i)
while indexex.isEmpty() == False:
    tmpI = indexex.pop()
    seeFront[tmpI] = len(towers) - 1 - tmpI
towers.reverse()
myStack = Stack()
indexex = Stack()
myStack.push(towers[0])
indexex.push(0)
for i in range(0,len(towers)):
    if myStack.isEmpty() == True:
        myStack.push(towers[i])
        indexex.push(i)
        continue
    if(myStack.isEmpty() == False):
        while(True):
            if((myStack.isEmpty() == True) or (myStack.peek() >= towers[i])):
                break
            tmpI = indexex.pop()
            myStack.pop()
            seeBack[tmpI] = i - tmpI
        myStack.push(towers[i])
        indexex.push(i)

while indexex.isEmpty() == False:
    tmpI = indexex.pop()
    seeBack[tmpI] = len(towers) - 1 - tmpI
seeBack.reverse()
print (seeFront)
print (seeBack)
for i in range(0,n):
    print(max(seeFront[i], seeBack[i]), end=' ')
