def calculate_square():
	i = 1	
	while True:
		yield i*i
		i+=1

for get_sq in calculate_square():
	print(get_sq)
	if get_sq >= 100:
		break
