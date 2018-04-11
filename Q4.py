#Jennifer Fung A12099804
filename = "datafile.txt"
f = open(filename, "r")
w = open("pa1_4.txt", "w")
for line in f:
	line = line.strip()
	line = line.lower()
	if ">" in line:
		if "rat" in line:
			header = True
			print(line)
			w.write(line + "\n")
		if "mus" in line:
			header = True
			print(line)
			w.write(line + "\n")
	else:
		if header == True:
			line = line.upper()
			print(line[0:60])
			w.write(line[0:60])
			ok = True
	#not sure how to turn off booleans without turning it off before where we want it....uhhh
	#if ok == True:
	#	header = False
