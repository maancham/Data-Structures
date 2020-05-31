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
mines = list(int(i) for i in input().split())
mines.append(-1)
n += 1
clan_inventory = []
seeFront = [0 for i in range(n)]
temp_arr = [0 for i in range(100000000)]

for i in range(0, n):
    temp_arr[mines[i] - 1] += 1

for i in range(0,n):
    clan_inventory.append(temp_arr[mines[i] - 1])

for i in range(n):
    if myStack.isEmpty() :
        myStack.push(clan_inventory[i])
        indexex.push(i)
        continue
    else :
        while(True):
            if(myStack.isEmpty() or (myStack.peek() >= clan_inventory[i])):
                break
            tmpI = indexex.pop()
            myStack.pop()
            seeFront[tmpI] = i - tmpI
        myStack.push(clan_inventory[i])
        indexex.push(i)
while not indexex.isEmpty() :
    tmpI = indexex.pop()
    seeFront[tmpI] = len(clan_inventory) - 1 - tmpI

for i in range(n-1):
    print(mines[seeFront[i] + i], end=' ')
print()





