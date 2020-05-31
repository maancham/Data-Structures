def trip(limit, weights, val, n): 
	if (n == 0) or (limit == 0): 
		return 0
	if (weights[n-1] > limit): 
		return trip(limit, weights, val, n-1) 
	else:
        next_move =  max(val[n-1] + trip(limit-weights[n-1], weights, val, n-1), trip(limit, weights, val, n-1))  
		return next_move
 
first_line = list(input().split())
weight_limit = int(first_line[0])
values = list(map(int, input().split()))
n = len(values)
weights = list(map(int, input().split()))
print (trip(weight_limit,weights,values,n))



