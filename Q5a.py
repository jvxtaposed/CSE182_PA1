#Jennifer Fung A12099804
filename = "datafile.txt"
f = open(filename, "r")
wSeq = open("data.seq", "w")
for line in f:
	line = line.strip()
	if ">" in line:
		wSeq.write("@")
		print("@", end='')
	else:
		wSeq.write(line)
		print(line, end='')

