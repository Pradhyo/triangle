total = 0
offset = 0
values = []

with open('sample.txt') as fp:
	for line in fp:
		x = line.split()
		x = map (int,x)
		values.append(x)