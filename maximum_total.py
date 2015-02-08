from collections import defaultdict
values = []
mem_max = defaultdict(lambda:defaultdict(list))

'''Store given values from file in a list of lists'''
with open('triangle.txt') as fp:
	for line in fp:
		x = line.split()
		x = map(int,x)
		values.append(x)

'''Loop from bottom to top, looping through each element of a row
   solving each sub-problem until the top'''
for row in range(len(values)-1,-1,-1):
	for column in range(len(values[row])):
		mem_max[row][column] = values[row][column]	
		if row != len(values)-1:
			mem_max[row][column] += max(mem_max[row+1][column],mem_max[row+1][column+1])

print mem_max[0][0]