total = 0
offset = 0

with open('sample.txt') as fp:
	for line in fp:
		x = line.split()
		if len(x) > 1:
			if int(x[offset]) < int(x[offset+1]):
				offset = offset + 1
		total = total + int(x[offset])
print total

	