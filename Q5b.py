#Jennifer Fung A12099804
filename = "datafile.txt"
f = open(filename, "r")
w = open("data.in", "w")
counter = 0
seq = ""
for line in f:
	line = line.strip()
	if ">" not in line:
		seq += line
	if ">" in line:
		offset = len(seq)
		gi = line[line.find("|")+1:line.find("|", 4 )]
		output = gi + " " + str(offset) + "\n"
		print(output)
		w.write(output)
