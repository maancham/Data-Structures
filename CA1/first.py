w, h = 6, 6;
matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
	content = input().split()
	for j in range(w):
		content[j] = int(content[j])
	matrix[i] = content
max_sum = 0
new_max = 0
for i in range(1,w-1):
	for j in range(1,w-1):
		new_max = matrix[i-1][j-1]+matrix[i-1][j]+matrix[i-1][j+1]+matrix[i][j]+matrix[i+1][j-1] + matrix[i+1][j]+matrix[i+1][j+1]
		if(new_max > max_sum):
			max_sum = new_max
print(max_sum)


