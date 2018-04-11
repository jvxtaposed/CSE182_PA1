#Jennifer Fung A12099804
#read in the files
filename = "datafile.txt"
f = open(filename, "r")
w = open("pa1_3.txt", "w")
seq = ""


for line in f:
    line = line.strip()
    # cat all sequence into one line and then count the length
    if ">" not in line:
        seq += line
    #if HEADER, then
    else:
        print(len(seq))
        seqLen = len(seq)
        seq = ""
        header = line
        output = header + " " + str(seqLen) + "\n"
        print(header)
print(len(seq))
