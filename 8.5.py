fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if 'From' in line:
        if 'From:' not in line:
            count = count + 1
            print(line.split()[1])
print("There were", count, "lines in the file with From as the first word")
