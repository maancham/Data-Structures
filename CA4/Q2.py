def change_mode(status,index):
    if (status[index] == 0):
        status[index] = 1
    else:
        status[index] = 0

def toggle(array,status,index):
    distance = len(array[index])
    for j in range(distance):
        change_mode(status,array[index][j])
    change_mode(status,index)



def show_report(array,status,index):
    sum = 0
    goal = index - 1
    sum += status[index]
    distance = len(array[index])
    for j in range(distance):
        if(status[array[index][j]] == 1):
            sum += 1
    return sum

n = int(input())
ancestors = list(map(int, input().split()))
status = list(map(int, input().split()))
k = int(input())

array = [[] for m in range(n)]
for j in range(n-1,0,-1):
    goal = ancestors[j-1] - 1
    array[goal].append(j)
    fill_distance = len(array[j])
    for i in range(fill_distance):
        new_child = array[j][i]
        array[goal].append(new_child)


for i in range(k):
    command , num = input().split()
    if (command == "report"):
        print(show_report(array,status,int(num)-1))
    else:
        toggle(array,status,int(num)-1)