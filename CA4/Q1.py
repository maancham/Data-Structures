import math
import heapq

first_line = list(input().split())
n = int(first_line[0])
t = int(first_line[1])
output = 0
tree = [-1 *int(j) for j in input().split()]
heapq.heapify(tree)
for i in range(t):
    removed_el = heapq.heappop(tree)
    modified_el = -1 * math.floor(-1 * removed_el / 2)
    heapq.heappush(tree,modified_el)
    output += removed_el
print(-1 * output)

