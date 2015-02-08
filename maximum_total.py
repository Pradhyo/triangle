from collections import defaultdict
total = 0
offset = 0
values = []
mem_max = defaultdict(lambda:defaultdict(list))

def max_total(row,column):
	if mem_max[row][column]:
		return mem_max[row][column]
	else:
		if row == len(values)-1:
			mem_max[row][column] = values[row][column]
		else:
			mem_max[row][column] = values[row][column] + max(max_total(row+1,column),max_total(row+1,column+1))
		
		return mem_max[row][column]
		

with open('triangle.txt') as fp:
	for line in fp:
		x = line.split()
		x = map(int,x)
		values.append(x)

print max_total(0,0)