import math

def inorder(array, inorder_list, index, n) :
    if index >= n :
        return
    inorder(array, inorder_list, 2 * index + 1, n)  
    inorder_list.append(array[index])
    inorder(array, inorder_list, 2 * index + 2, n) 

n = int(input())
first_array = [int(data) for data in input().split()]

in_order_array = []
inorder(first_array, in_order_array, 0, n)

in_order = zip(in_order_array, [i for i in range(n)])
in_order = sorted(in_order, key=lambda t: t[0])

changesNumber = 0
i = 0
while i < n :
    prevIndex = in_order[i][1]
    if i == prevIndex :
        i += 1
        continue
    else :
        in_order[i] , in_order[prevIndex] = in_order[prevIndex] , in_order[i]
    if i != in_order[i][1] :
        i -= 1
    changesNumber += 1
    i += 1

print(changesNumber)