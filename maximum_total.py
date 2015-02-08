from collections import defaultdict
total = 0
offset = 0
values = []
mem_max = defaultdict(lambda:defaultdict(list))

with open('triangle.txt') as fp:
	for line in fp:
		x = line.split()
		x = map(int,x)
		values.append(x)

for row in range(len(values)-1,-1,-1):
	for column in range(len(values[row])):
		if row == len(values)-1:
			mem_max[row][column] = values[row][column]
		else:
			mem_max[row][column] = values[row][column] + max(mem_max[row+1][column],mem_max[row+1][column+1])


print mem_max[0][0]