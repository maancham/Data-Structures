
def DFS(ln,graph,v,visited):  
    visited[v]= 1
    max_len = ln
    for i in graph[v]: 
        if (visited[i]==0): 
            temp =  DFS(ln + 1,graph,i,visited)
            if (temp > max_len):
                max_len = temp
    visited[v] = 0
    return max_len

def check_hamil(graph,n): 
    visited =[0]*n 
    max_path = 0
    for i in range(n): 
        temp = DFS(1,graph,i,visited) 
        if (max_path < temp):
            max_path = temp
    if (max_path == n):
        return True
    return False


n = int(input())
word_list = []
graph = [[] for i in range (n)]
for i in range(n):
    node = input()
    word_list.append(node)

for j in range(len(word_list)) :
    for k in range(len(word_list)) :
        if (word_list[k][0] == word_list[j][len(word_list[j]) - 1]):
            graph[j].append(k)
            
if (check_hamil(graph,n) == False):
    print("not possible")    
else:
    print("possible")

