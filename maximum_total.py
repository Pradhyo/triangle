total = 0
offset = 0
values = []

def max(row,column):
	if row == len(values)-1:
		return values[row][column]
	elif max(row+1,column) > max(row+1,column+1):
		return values[row][column]+max(row+1,column)
	else:
		return values[row][column] + max(row+1,column+1)

with open('sample.txt') as fp:
	for line in fp:
		x = line.split()
		x = map (int,x)
		values.append(x)

print max(0,0)