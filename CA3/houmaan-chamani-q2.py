arr = list(int(i) for i in input().split())
positions = list(int(i) for i in input().split())
n = arr[0]
k = arr[1]
temp_array = []
for i in range(0,k):
    temp_array.append(0)
sum = 0
ans = 0
for i in range(len(positions)):
    positions[i] += sum
    positions[i] %= 3
    temp_array.append((3 - positions[i])%3) 
    sum += temp_array[-1] - temp_array[-k]
    ans += temp_array[-1]

print(ans)
