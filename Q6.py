#Jennifer Fung A12099804
dataSeq = "data.seq"
dataIn = "data.in"
dS = open(dataSeq, "r")
dI = open(dataIn, "r")
w = open("pa1_6.txt", "w")
array = []
#openning dataIn as list
with open(dataIn) as f:
	for line in f:
		array.append([int(x) for x in line.split()])
		#print array

#reads it in & turns it into lowercase so theres a baseline
Seq = dS.readline()


query = "MHIQITDFGTAKVLSPDS"
if query in Seq:
	#print("yay")
	found = Seq.index(query)
	#print found
	for line in array:
	#print line[1]
		if found > line[1]:
			prev = True
			prevIn = line[1]
			prevInG = line[0]
		elif found < line[1]:
			prev = False
			output = "input: " + str(query) + "\n" +  "gi number: " + str(prevInG)
print (output)
w.write(output)
