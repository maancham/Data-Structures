def BFS(network,indexes,source,dest):
    new_arr = []
    for i in range(len(indexes)):
        if(source in indexes[i]):
           s = i
    new_arr.append([s,1])
    while(new_arr):
        top = new_arr.pop(0)
        if (dest in indexes[top[0]]):
            return(top[1])
        else:
            for i in network[top[0]]:
                new_arr.append([i, top[1] + 1])
    return -1
    
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if len(a_set.intersection(b_set)) > 0: 
        return(True)  
    return(False)


n =  int(input())
network = {}
indexes = []
for i in range(n):
    network[i] = []
for m in range(n) :
    bus_stops = list(map(int,input().split()))
    indexes.append(bus_stops)
for i in range (n):
    for j in range(i+1,n):
        if (common_member(indexes[i],indexes[j])) :
            network[i].append(j)
            network[j].append(i)
source , dest = list(map(int,input().split()))

print(BFS(network,indexes,source,dest))
