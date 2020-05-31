def first_method(books,max_borrow):
	returns_needed = 0
	n = max_borrow
	inventory = []
	for i in range(len(books)):
		if (inventory.count(books[i]) == 0)and(len(inventory) < n):
			returns_needed += 1
			inventory.append(books[i])
		elif (len(inventory) == n)and(inventory.count(books[i]) == 0):
			inventory.pop(0)
			inventory.append(books[i])
			returns_needed += 1	
	print(returns_needed)

def second_method(books,max_borrow):
	returns_needed = 0
	n = max_borrow
	inventory = []
	for i in range(len(books)):
		if (inventory.count(books[i]) == 0)and(len(inventory) < n):
			returns_needed += 1
			inventory.append(books[i])
		elif (len(inventory) == n)and(not(books[i] in inventory)):
			books_ahead = books[i:]
			index_num = 0
			max = 0
			for j in range(len(inventory)):
				
				if not(inventory[j] in books_ahead):
					index_num = j
					break
				else:
					place = books_ahead.index(inventory[j])
					if (place > max):
						max = place
						index_num = j
			inventory.pop(index_num)
			returns_needed += 1
			inventory.append(books[i])
	print(returns_needed)


def third_method(books,max_borrow):
	returns_needed = 0
	n = max_borrow
	inventory = []
	for i in range(len(books)):
		if (inventory.count(books[i]) == 0)and(len(inventory) < n):
			returns_needed += 1
			inventory.append(books[i])
		elif (len(inventory) == n)and(inventory.count(books[i]) == 0):
			inventory = inventory[1:len(inventory)]
			inventory.append(books[i])
			returns_needed += 1
		elif(books[i] in inventory):
			inventory.remove(books[i])
			inventory.append(books[i])

	print(returns_needed)				


books = input().split("-")
books = list(map(int, books))
max_borrow = input()
method = input()
if (method == "1"):
	first_method(books,int(max_borrow))
elif (method == "2"):
	second_method(books,int(max_borrow))
elif (method == "3"):
	third_method(books,int(max_borrow))
