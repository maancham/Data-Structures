def BFS(game,m,n):
    new_arr = []
    visited = [0] * len(game)
    visited.append(0)
    new_arr.append([0,0])
    while(new_arr):
        top = new_arr.pop(0)
        if (top[0] == (m*n -1)):
            return(top[1])
        else:
            for i in game[top[0]]:
                if not (i in visited):
                    new_arr.append([i, top[1] + 1])
                    visited.append(i)

first_line = input().split()
next_lines = input().split()
n = int(first_line[0])
m = int(first_line[1])
size = n * m
deadline = [-1,-1,-1]
game = [[] for i in range (size)]
alterate = [0] * size
while (next_lines != deadline):
    i = int(next_lines[0])
    j = int(next_lines[1]) 
    dst = int(next_lines[2])
    first_key = n - i - 1
    second_key = m - j -1
    if (first_key % 2 == 1):
        desired_index = first_key * m + second_key
    else:
        desired_index = first_key * m + j    
    alterate[desired_index] = dst
    next_lines = list(map(int,input().split()))
for k in range (size):
    for p in range (6):
        key = k + p + 1
        if (key < size):
            new_element  = alterate[key]
            if (new_element ==  0):
                    if key not in game[k]:
                        game[k].append(key)
            else:
                if new_element not in game[k]:
                    game[k].append(new_element)

print(BFS(game,m,n))


